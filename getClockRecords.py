import sqlite3
import requests
import logging
import json


def getClockRecords():
    connection = sqlite3.connect("./database.sqlite")
    cursor = connection.cursor()

    cursor.execute("""
     DELETE FROM records WHERE name LIKE '%y%';
     """)
    print('deleted')

    # add a table for records to sqlite3

    # cursor.execute("""
    #  CREATE TABLE IF NOT EXISTS records (
    #  id VARCHAR(255) PRIMARY KEY,
    #  tag VARCHAR(255),
    #  type VARCHAR(255),
    #  country_iso VARCHAR(8),
    #  country_name VARCHAR(255),
    #  attemptResult VARCHAR(255),
    #  name VARCHAR(255),
    #  event VARCHAR(255),
    #  eventId VARCHAR(255),
    #  competitionId VARCHAR(255),
    #  competitionName VARCHAR(255),
    #  roundId VARCHAR(255)
    #  )
    #  """)

    connection.commit()

    def getRecentRecords():
        try:
            response = requests.post(url="https://live.worldcubeassociation.org/api/graphql", json={
                "query": """
              {
                recentRecords {
                  id
                  type
                  tag
                  attemptResult
                  result {
                    person {
                      name
                      id
                      country {
                        iso2
                        name
                      }
                    }
                    round {
                      id
                      competitionEvent {
                        event{
                          id
                          name
                        }
                        competition {
                          id
                          name
                        }
                      }
                    }
                  }
                }
              }
            """
            }
                                     )

            allRecords = json.loads(response.text)["data"]["recentRecords"]
            # filter to only clock results
            records = [x for x in allRecords if x['result']['round']['competitionEvent']['event']['name'] == 'Clock']
            # records = [x for x in allRecords if x['result']['person']['country']['name'] == 'Canada']
            # for record in records:
            #     print(record['result']['person']['name'], record['tag'], record['result']['person']['country']['name'],
            #           record['attemptResult'], record['type'])

            for record in records:
                if not cursor.execute("SELECT * FROM records WHERE id = ?", (record["id"],)).fetchall():
                    cursor.execute(
                        "INSERT INTO records (id, tag, type, country_name, attemptResult, name, event, competitionName) VALUES (?, ?, ?, ?, ?, ?, ?, ?)",
                        (record["id"], record["tag"], record["type"], record["result"]["person"]["country"]["name"],
                         record["attemptResult"], record["result"]["person"]["name"],
                         record["result"]["round"]["competitionEvent"]["event"]["name"],
                         record["result"]["round"]["competitionEvent"]["competition"]["name"]))
                    print("added:\n" + json.dumps(record))
                else:
                    print("exists " + json.dumps(record["result"]["person"]["name"]))

        except Exception as e:
            logging.error(f"An error occurred: {e}")

    getRecentRecords()
    connection.commit()
    connection.close()
