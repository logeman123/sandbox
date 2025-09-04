#!/usr/bin/env python3
"""
Script to process ALL 930 records from the complete CachedJson file
This is the CORRECT approach to handle your complete dataset
"""

import json
import csv
import sys

def process_complete_cached_json(file_path):
    """
    Process the complete CachedJson file with all 930 records
    
    Args:
        file_path: Path to the complete JSON file
    """
    
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract the complete value string
        cached_json = data['CachedJson'][0]['value']
        
        # Parse the complete embedded JSON with all 930 records
        all_records = json.loads(cached_json)
        
        print(f"✅ Successfully loaded {len(all_records)} records")
        
        # Create CSV with all records
        output_file = 'all_930_trading_rankings.csv'
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ranking', 'username', 'account_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Process ALL records
            for record in all_records:
                ranking = record.get('ranking', '')
                nickname = record.get('nickname')
                username = nickname if nickname is not None else ''
                account_id = record.get('account_id', '')
                
                writer.writerow({
                    'ranking': ranking,
                    'username': username,
                    'account_id': account_id
                })
        
        # Verify the output
        with open(output_file, 'r') as f:
            line_count = sum(1 for line in f)
        
        print(f"🎉 SUCCESS!")
        print(f"📄 Created: {output_file}")
        print(f"📊 Total lines: {line_count} (including header)")
        print(f"📈 Data records: {line_count - 1}")
        print(f"✅ Expected: 930+ records")
        
        if line_count - 1 >= 930:
            print("✅ CORRECT: All 930+ records processed!")
        else:
            print("❌ ISSUE: Missing records - need complete JSON file")
        
        return output_file
        
    except FileNotFoundError:
        print(f"❌ File not found: {file_path}")
        print("💡 Please provide the complete CachedJson file")
        return None
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return None
    except Exception as e:
        print(f"❌ Error: {e}")
        return None

def main():
    print("🎯 COMPLETE 930-RECORD CSV CONVERTER")
    print("=" * 50)
    
    # Try to process the complete file
    input_file = 'CachedJson_202509041508.json'
    
    print(f"📁 Looking for: {input_file}")
    
    result = process_complete_cached_json(input_file)
    
    if not result:
        print("\\n🚨 TO FIX THIS ISSUE:")
        print("=" * 30)
        print("1. Your attached file has 930 records in the 'value' field")
        print("2. I need the COMPLETE JSON file with all that data")
        print("3. Or provide the complete 'value' string content")
        print("\\n📝 The 'value' field should contain a JSON array with 930 objects")
        print("   Each object should have: ranking, nickname, account_id, etc.")
        
        print("\\n💡 Once I have the complete data, I'll create:")
        print("   ✅ CSV with exactly 930+ rows (plus header)")
        print("   ✅ Columns: ranking, username, account_id")
        print("   ✅ Proper handling of null usernames")

if __name__ == "__main__":
    main()