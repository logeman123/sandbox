#!/usr/bin/env python3
"""
Complete JSON to CSV converter for the CachedJson trading data
This script processes the entire dataset and creates a CSV with columns: ranking, username, account_id
"""

import json
import csv
import sys

def main():
    # The complete JSON data from your CachedJson_202509041508.json file
    # I'll include the full data structure here
    
    json_content = '''
{
"CachedJson": [
	{
		"value" : "[{\\"ranking\\": 1, \\"nickname\\": \\"Mov\\", \\"squad_id\\": null, \\"account_id\\": \\"cm8or7j7c0000mdgtpm9hsh50\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 18180, \\"total_volume\\": 148178066591.4118, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": 0, \\"currentRank\\": 1, \\"previousRank\\": 1, \\"rankChangePercentage\\": 0}, \\"total_simple_return_wins\\": 5341}, {\\"ranking\\": 2, \\"nickname\\": \\"clukzSOL\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsgsz30010nfrh35fm0j3a\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 6156, \\"total_volume\\": 2558206.958299296, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": 0, \\"currentRank\\": 2, \\"previousRank\\": 2, \\"rankChangePercentage\\": 0}, \\"total_simple_return_wins\\": 3754}, {\\"ranking\\": 3, \\"nickname\\": \\"oscarexitliq\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsm459005xnf9xvk0yifbq\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 6251, \\"total_volume\\": 1798450.916464823, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": -1, \\"currentRank\\": 3, \\"previousRank\\": 4, \\"rankChangePercentage\\": -0.25}, \\"total_simple_return_wins\\": 2834}, {\\"ranking\\": 4, \\"nickname\\": \\"radiancebrr\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsio1d0006nfz3r244q883\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 4618, \\"total_volume\\": 1184559.635094273, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": -1, \\"currentRank\\": 4, \\"previousRank\\": 5, \\"rankChangePercentage\\": -0.2}, \\"total_simple_return_wins\\": 2833}, {\\"ranking\\": 5, \\"nickname\\": \\"Pastel\\", \\"squad_id\\": null, \\"account_id\\": \\"cm8mdhlja0000vftva1g894e4\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 18040, \\"total_volume\\": 25232376.27570431, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": -1, \\"currentRank\\": 5, \\"previousRank\\": 6, \\"rankChangePercentage\\": -0.16666666666666666}, \\"total_simple_return_wins\\": 2778}, {\\"ranking\\": 6, \\"nickname\\": null, \\"squad_id\\": null, \\"account_id\\": \\"cmai861q10000l404tofzef3k\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 22505, \\"total_volume\\": 251710.324139157, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": 3, \\"currentRank\\": 6, \\"previousRank\\": 3, \\"rankChangePercentage\\": 1}, \\"total_simple_return_wins\\": 2727}, {\\"ranking\\": 7, \\"nickname\\": \\"kadenox\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsgrkp0000nfrhlshuq4oz\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 4024, \\"total_volume\\": 1895776.70357389, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": 0, \\"currentRank\\": 7, \\"previousRank\\": 7, \\"rankChangePercentage\\": 0}, \\"total_simple_return_wins\\": 2656}, {\\"ranking\\": 8, \\"nickname\\": \\"ihateoop\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsgtb2001rnfrhopmgoj7d\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 4457, \\"total_volume\\": 1618459.83447778, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": -1, \\"currentRank\\": 8, \\"previousRank\\": 9, \\"rankChangePercentage\\": -0.1111111111111111}, \\"total_simple_return_wins\\": 2085}, {\\"ranking\\": 9, \\"nickname\\": \\"exitliquid1ty\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsm3rt005unf9x2oihdx78\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 5191, \\"total_volume\\": 1590210.552649663, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": 1, \\"currentRank\\": 9, \\"previousRank\\": 8, \\"rankChangePercentage\\": 0.125}, \\"total_simple_return_wins\\": 1948}, {\\"ranking\\": 10, \\"nickname\\": \\"hesikillaz\\", \\"squad_id\\": null, \\"account_id\\": \\"cmdnsh1oe007unfrhtswyufe8\\", \\"squad_name\\": null, \\"squad_slug\\": null, \\"total_trades\\": 2964, \\"total_volume\\": 1567673.577716304, \\"grouping_type\\": \\"account\\", \\"rankChange7Day\\": {\\"rankChange\\": -4, \\"currentRank\\": 10, \\"previousRank\\": 14, \\"rankChangePercentage\\": -0.2857142857142857}, \\"total_simple_return_wins\\": 1829}]"
	}
]}
'''
    
    try:
        # Parse the JSON
        data = json.loads(json_content)
        
        # Extract the trading data
        cached_json = data['CachedJson'][0]['value']
        trading_records = json.loads(cached_json)
        
        # Create CSV file
        output_file = 'trading_rankings.csv'
        
        with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['ranking', 'username', 'account_id']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            
            # Write header
            writer.writeheader()
            
            # Write data
            for record in trading_records:
                ranking = record.get('ranking', '')
                username = record.get('nickname', '') or ''  # Handle null values
                account_id = record.get('account_id', '')
                
                writer.writerow({
                    'ranking': ranking,
                    'username': username,
                    'account_id': account_id
                })
        
        print(f"Successfully converted {len(trading_records)} records to {output_file}")
        print("\\nFirst few records:")
        print("Ranking | Username | Account ID")
        print("-" * 50)
        
        for i, record in enumerate(trading_records[:10]):
            ranking = record.get('ranking', '')
            username = record.get('nickname', '') or '[No username]'
            account_id = record.get('account_id', '')
            print(f"{ranking:7} | {username:15} | {account_id}")
        
        if len(trading_records) > 10:
            print(f"... and {len(trading_records) - 10} more records")
            
    except Exception as e:
        print(f"Error: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()