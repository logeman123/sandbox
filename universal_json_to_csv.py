#!/usr/bin/env python3
"""
Universal JSON to CSV converter for CachedJson trading data
This script can process any CachedJson file and extract ranking, username, and account_id
"""

import json
import csv
import sys
import os

def process_cached_json_file(input_file, output_file):
    """
    Process a CachedJson file and convert to CSV
    
    Args:
        input_file: Path to the input JSON file
        output_file: Path to the output CSV file
    """
    
    try:
        # Read the JSON file
        with open(input_file, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        # Extract the CachedJson data
        cached_json = data.get('CachedJson', [])
        if not cached_json:
            print("❌ No CachedJson array found in the file")
            return False
        
        # Get the value string (which contains the actual trading data as JSON)
        value_string = cached_json[0].get('value', '[]')
        
        # Parse the embedded JSON
        trading_records = json.loads(value_string)
        
        # Create the CSV file
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ranking', 'username', 'account_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Process each trading record
            for record in trading_records:
                ranking = record.get('ranking', '')
                nickname = record.get('nickname')
                username = nickname if nickname is not None else ''
                account_id = record.get('account_id', '')
                
                writer.writerow({
                    'ranking': ranking,
                    'username': username,
                    'account_id': account_id
                })
        
        # Report results
        print(f"✅ Successfully processed {len(trading_records)} records")
        print(f"📄 Output file: {output_file}")
        print(f"📊 Columns: ranking, username, account_id")
        
        # Count records with/without usernames
        with_username = sum(1 for r in trading_records if r.get('nickname'))
        without_username = len(trading_records) - with_username
        
        print(f"\\n📈 Data summary:")
        print(f"   Records with username: {with_username}")
        print(f"   Records without username: {without_username}")
        print(f"   Total records: {len(trading_records)}")
        
        # Show sample of top rankings
        print(f"\\n🏆 Top 10 rankings:")
        print("   Rank | Username           | Account ID")
        print("   " + "-" * 55)
        
        for record in trading_records[:10]:
            ranking = record.get('ranking', '')
            username = record.get('nickname', '') or '[No username]'
            account_id = record.get('account_id', '')[:20] + '...'  # Truncate for display
            print(f"   {ranking:4} | {username:18} | {account_id}")
        
        return True
        
    except FileNotFoundError:
        print(f"❌ File not found: {input_file}")
        return False
    except json.JSONDecodeError as e:
        print(f"❌ JSON parsing error: {e}")
        return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    # Check if input file is provided as command line argument
    if len(sys.argv) > 1:
        input_file = sys.argv[1]
        output_file = sys.argv[2] if len(sys.argv) > 2 else 'trading_rankings.csv'
    else:
        # Default files
        input_file = 'CachedJson_202509041508.json'
        output_file = 'trading_rankings.csv'
    
    print("🚀 CachedJson to CSV Converter")
    print("=" * 40)
    print(f"Input file:  {input_file}")
    print(f"Output file: {output_file}")
    print()
    
    # Check if input file exists
    if not os.path.exists(input_file):
        print(f"❌ Input file '{input_file}' does not exist")
        print("\\n💡 Usage:")
        print(f"   python3 {sys.argv[0]} <input_json_file> [output_csv_file]")
        print("\\n   Example:")
        print(f"   python3 {sys.argv[0]} CachedJson_202509041508.json trading_rankings.csv")
        sys.exit(1)
    
    # Process the file
    success = process_cached_json_file(input_file, output_file)
    
    if success:
        print(f"\\n🎉 Conversion completed successfully!")
        print(f"📁 Your CSV file is ready: {output_file}")
    else:
        print(f"\\n💥 Conversion failed!")
        sys.exit(1)

if __name__ == "__main__":
    main()