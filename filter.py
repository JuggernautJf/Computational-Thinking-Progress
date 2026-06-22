import io
import pandas as pd

df = pd.read_csv('Scores.dataset.csv', skipinitialspace=True)

month_map = {
    "Jan": 1,
    "Feb": 2,
    "Mar": 3,
    "Apr": 4,
    "May": 5,
    "Jun": 6,
    "Jul": 7,
    "July": 7,
    "Aug": 8,
    "Sep": 9,
    "Oct": 10,
    "Nov": 11,
    "Dec": 12,
}

def main() -> None:
    print("---bucketScores---")
    bucketTotal()
    print("---bucketBirthDay---")
    bucketBirthDay()
    print("---minMarks---")
    minMarks()

def minMarks() -> None:
    print(f"A: {df['Mathematics'].min()}")
    print(f"B: {df['Physics'].min()}")

def bucketBirthDay() -> None:
    df["Month_num"] = df["DateOfBirth_m"].map(month_map)

    df["DOB"] = pd.to_datetime(
            df["DateOfBirth_d"].astype(str) + "-" + df["Month_num"].astype(str) + "-2006",
            format="%d-%m-%Y"
    )

    #Dates for comparison
    may_1 = pd.to_datetime("01-05-2006", format="%d-%m-%Y")
    apr_30 = pd.to_datetime("30-04-2006", format="%d-%m-%Y")
    sep_1 = pd.to_datetime("01-09-2006", format="%d-%m-%Y")
    aug_31 = pd.to_datetime("31-08-2006", format="%d-%m-%Y")

    # Apply the condition counts
    A = len(df[df["DOB"] < may_1])
    B = len(df[(df["DOB"] > apr_30) & (df["DOB"] < sep_1)])
    C = len(df[df["DOB"] > aug_31])

    print(f"A = {A}")
    print(f"B = {B}")
    print(f"C = {C}")

def bucketTotal() -> None:

    df_A = df[df["Total"] > 250]
    A_count = len(df_A)  # or df_A.shape[0]

    # B: Number of Cards with 250 > Total > 200
    df_B = df[(df["Total"] < 250) & (df["Total"] > 200)]
    B_count = len(df_B)

    # C: Number of Cards with 200 > Total > 0
    df_C = df[(df["Total"] < 200) & (df["Total"] > 0)]
    C_count = len(df_C)

    print(f"A (Total > 250): {A_count} cards")
    print(f"B (250 > Total > 200): {B_count} cards")
    print(f"C (200 > Total > 0): {C_count} cards")




if __name__ == "__main__":
    main()