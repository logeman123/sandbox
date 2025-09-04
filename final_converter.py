#!/usr/bin/env python3
"""
Final converter to process the complete CachedJson file and create CSV
"""

import json
import csv

def convert_cached_json_to_csv(json_file_path, csv_file_path):
    """
    Convert the CachedJson file to CSV format
    
    Args:
        json_file_path: Path to the input JSON file
        csv_file_path: Path to the output CSV file
    """
    
    try:
        # Read the JSON file
        with open(json_file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract the CachedJson value
        cached_json = data.get('CachedJson', [])
        if not cached_json:
            raise ValueError("No CachedJson found in the file")
        
        # Parse the embedded JSON string
        json_string = cached_json[0].get('value', '[]')
        records = json.loads(json_string)
        
        # Create CSV file
        with open(csv_file_path, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ranking', 'username', 'account_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Process each record
            for record in records:
                ranking = record.get('ranking', '')
                username = record.get('nickname', '') or ''  # Handle null values
                account_id = record.get('account_id', '')
                
                writer.writerow({
                    'ranking': ranking,
                    'username': username,
                    'account_id': account_id
                })
        
        print(f"✅ Successfully converted {len(records)} records to {csv_file_path}")
        
        # Show summary
        print(f"\\n📊 Summary:")
        print(f"   Total records: {len(records)}")
        print(f"   Output file: {csv_file_path}")
        print(f"   Columns: ranking, username, account_id")
        
        # Show first few records
        print(f"\\n🔍 First 5 records:")
        print("   Ranking | Username           | Account ID")
        print("   " + "-" * 55)
        
        for i, record in enumerate(records[:5]):
            ranking = record.get('ranking', '')
            username = record.get('nickname', '') or '[No username]'
            account_id = record.get('account_id', '')
            print(f"   {ranking:7} | {username:18} | {account_id}")
        
        # Show records with no username
        no_username_count = sum(1 for r in records if not r.get('nickname'))
        print(f"\\n📝 Records with no username: {no_username_count}")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ Error: File {json_file_path} not found")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    input_file = 'CachedJson_202509041508.json'
    output_file = 'trading_rankings.csv'
    
    print("🚀 Converting CachedJson to CSV...")
    print(f"   Input:  {input_file}")
    print(f"   Output: {output_file}")
    print()
    
    success = convert_cached_json_to_csv(input_file, output_file)
    
    if success:
        print(f"\\n✨ Conversion complete! Check {output_file}")
    else:
        print("\\n💥 Conversion failed!")

if __name__ == "__main__":
    main()