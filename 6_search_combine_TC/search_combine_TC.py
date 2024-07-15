import pandas as pd

# Read the reference and query dataframes
reference_df = pd.read_excel('/Users/calvincornell/UN15/Book1_modified.xlsx')
query_df = pd.read_excel('/Users/calvincornell/UN15/new_Modified_TC.xlsx')

# Function to check if a string has four decimal points
def has_four_decimal_points(string):
    decimal_count = string.count('.')
    return decimal_count == 4

# Separate complete and partial entries
complete_entries = query_df[query_df['TCDB'].apply(has_four_decimal_points)]
partial_entries = query_df[~query_df['TCDB'].apply(has_four_decimal_points)]

# Find matches for complete entries
complete_matches = pd.merge(complete_entries, reference_df, left_on='TCDB', right_on='TC', how='inner')

# Find matches for partial entries
partial_matches = pd.merge(partial_entries, reference_df, left_on='TCDB', right_on='TC', how='inner')

# Identify entries without a match in reference_df
no_match_reference = reference_df[~reference_df['TC'].isin(complete_matches['TC']) & ~reference_df['TC'].isin(partial_matches['TC'])]

# Create a Pandas Excel writer using XlsxWriter as the engine.
with pd.ExcelWriter('/Users/calvincornell/UN15/123Result.xlsx', engine='xlsxwriter') as writer:
    # Write each DataFrame to a separate worksheet
    complete_matches.to_excel(writer, sheet_name='Complete Matches', index=False)
    partial_matches.to_excel(writer, sheet_name='Partial Matches', index=False)
    no_match_reference.to_excel(writer, sheet_name='No Match in Reference', index=False)
