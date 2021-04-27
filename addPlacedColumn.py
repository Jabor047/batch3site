import sqlite3
import pandas as pd

def main():
    conn = sqlite3.connect('batch3.sqlite')
    sqlFetchQuery = """SELECT * FROM fellows"""
    df = pd.read_sql(sqlFetchQuery, conn)

    placed = ["alaroabubakarolayemi@yahoo.com", "wanjirustephany@gmail.com", "adakibet@gmail.com",
              "biniyam.mengist@gmail.com", "patrickojunde@gmail.com", "uwizeyejeann@gmail.com",
              "bessymukaria@gmail.com", "gkkarobia@gmail.com", "kiiru.anastasia@gmail.com",
              "s.mwikali.muoki@gmail.com", "Amureridwan002@gmail.com", "munyolec@gmail.com",
              "smlnegash@gmail.com", "okiomagerald@gmail.com", "brianodhiambo530@gmail.com",
              "komboelvis08@gmail.com", "haddyadnan@gmail.com", "ilekuraidowu@gmail.com",
              "nabeelseid@gmail.com", "smslmuluwork@gmail.com", "natananshiferaw@gmail.com",
              "leonahoms@hotmail.com", "ogunfoworalawal@gmail.com", "rahelweldegebriel2120@gmail.com"]

    df['placed'] = df.apply(lambda x: x['email'] in placed, axis=1).astype(int)
    df.to_sql("fellowsWithPlaced", conn, if_exists="replace", index=False)

    sqlFetchQuery2 = """SELECT * FROM fellowsWithPlaced"""
    dfP = pd.read_sql(sqlFetchQuery2, conn)
    print(dfP.tail())

if __name__ == "__main__":
    main()
