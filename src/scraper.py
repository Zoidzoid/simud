"""
Real Web Scraper for Serie D standings
Parses actual data from the best available source
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime
import re


class SerieD_RealScraper:
    def __init__(self, source='flashscore'):
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        self.timeout = 15
        self.source = source
    
    def parse_flashscore_standings(self, html_content):
        """
        Parse standings from Flashscore HTML
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            groups_data = {}
            
            # Look for group tables
            tables = soup.find_all('table')
            
            if not tables:
                print("No tables found on Flashscore")
                return None
            
            # Parse each group (A01-A16)
            group_counter = 0
            for table in tables[:16]:  # Assuming first 16 tables are groups
                group_key = f"A{str(group_counter + 1).zfill(2)}"
                rows = table.find_all('tr')[1:]  # Skip header
                
                group_teams = []
                for idx, row in enumerate(rows[:6]):  # 6 teams per group
                    cells = row.find_all('td')
                    if len(cells) >= 9:
                        team_data = {
                            "position": idx + 1,
                            "name": cells[1].text.strip(),
                            "matches_played": int(cells[2].text.strip()),
                            "wins": int(cells[3].text.strip()),
                            "draws": int(cells[4].text.strip()),
                            "losses": int(cells[5].text.strip()),
                            "goals_for": int(cells[6].text.strip()),
                            "goals_against": int(cells[7].text.strip()),
                            "goal_difference": int(cells[6].text.strip()) - int(cells[7].text.strip()),
                            "points": int(cells[8].text.strip())
                        }
                        group_teams.append(team_data)
                
                if group_teams:
                    groups_data[group_key] = group_teams
                    group_counter += 1
            
            return groups_data
        
        except Exception as e:
            print(f"Error parsing Flashscore: {e}")
            return None
    
    def parse_futebolinterior_standings(self, html_content):
        """
        Parse standings from FutebolInterior HTML
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            groups_data = {}
            
            # FutebolInterior structure may differ
            # Look for group divs or tables with specific classes
            
            tables = soup.find_all('table', class_='standings')
            
            if not tables:
                tables = soup.find_all('table')
            
            group_counter = 0
            for table in tables[:16]:
                group_key = f"A{str(group_counter + 1).zfill(2)}"
                rows = table.find_all('tr')[1:]
                
                group_teams = []
                for idx, row in enumerate(rows[:6]):
                    cells = row.find_all('td')
                    if len(cells) >= 8:
                        team_data = {
                            "position": idx + 1,
                            "name": cells[1].text.strip(),
                            "matches_played": int(cells[2].text.strip()),
                            "wins": int(cells[3].text.strip()),
                            "draws": int(cells[4].text.strip()),
                            "losses": int(cells[5].text.strip()),
                            "goals_for": int(cells[6].text.strip()),
                            "goals_against": int(cells[7].text.strip()),
                            "goal_difference": int(cells[6].text.strip()) - int(cells[7].text.strip()),
                            "points": int(cells[-1].text.strip())
                        }
                        group_teams.append(team_data)
                
                if group_teams:
                    groups_data[group_key] = group_teams
                    group_counter += 1
            
            return groups_data
        
        except Exception as e:
            print(f"Error parsing FutebolInterior: {e}")
            return None
    
    def parse_ge_globo_standings(self, html_content):
        """
        Parse standings from GE Globo HTML
        """
        try:
            soup = BeautifulSoup(html_content, 'html.parser')
            groups_data = {}
            
            tables = soup.find_all('table')
            
            if not tables:
                print("No tables found on GE Globo")
                return None
            
            group_counter = 0
            for table in tables[:16]:
                group_key = f"A{str(group_counter + 1).zfill(2)}"
                rows = table.find_all('tr')[1:]
                
                group_teams = []
                for idx, row in enumerate(rows[:6]):
                    cells = row.find_all('td')
                    if len(cells) >= 8:
                        team_data = {
                            "position": idx + 1,
                            "name": cells[1].text.strip(),
                            "matches_played": int(cells[2].text.strip()),
                            "wins": int(cells[3].text.strip()),
                            "draws": int(cells[4].text.strip()),
                            "losses": int(cells[5].text.strip()),
                            "goals_for": int(cells[6].text.strip()),
                            "goals_against": int(cells[7].text.strip()),
                            "goal_difference": int(cells[6].text.strip()) - int(cells[7].text.strip()),
                            "points": int(cells[-1].text.strip())
                        }
                        group_teams.append(team_data)
                
                if group_teams:
                    groups_data[group_key] = group_teams
                    group_counter += 1
            
            return groups_data
        
        except Exception as e:
            print(f"Error parsing GE Globo: {e}")
            return None
    
    def scrape_flashscore(self):
        """Scrape Flashscore for Serie D standings"""
        print("Scraping Flashscore...")
        try:
            url = "https://www.flashscore.com/football/brazil/serie-d/standings/"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            standings = self.parse_flashscore_standings(response.content)
            
            if standings:
                print(f"✓ Successfully scraped {len(standings)} groups from Flashscore")
                return standings
            else:
                print("✗ Failed to parse Flashscore data")
                return None
        
        except Exception as e:
            print(f"✗ Flashscore scraping failed: {e}")
            return None
    
    def scrape_futebolinterior(self):
        """Scrape FutebolInterior for Serie D standings"""
        print("Scraping FutebolInterior...")
        try:
            url = "https://www.futebolinterior.com.br/campeonato/brasileirao-serie-d-2026/"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            standings = self.parse_futebolinterior_standings(response.content)
            
            if standings:
                print(f"✓ Successfully scraped {len(standings)} groups from FutebolInterior")
                return standings
            else:
                print("✗ Failed to parse FutebolInterior data")
                return None
        
        except Exception as e:
            print(f"✗ FutebolInterior scraping failed: {e}")
            return None
    
    def scrape_ge_globo(self):
        """Scrape GE Globo for Serie D standings"""
        print("Scraping GE Globo...")
        try:
            url = "https://ge.globo.com/futebol/brasileirao-serie-d/"
            response = requests.get(url, headers=self.headers, timeout=self.timeout)
            response.raise_for_status()
            
            standings = self.parse_ge_globo_standings(response.content)
            
            if standings:
                print(f"✓ Successfully scraped {len(standings)} groups from GE Globo")
                return standings
            else:
                print("✗ Failed to parse GE Globo data")
                return None
        
        except Exception as e:
            print(f"✗ GE Globo scraping failed: {e}")
            return None
    
    def scrape(self, fallback=True):
        """
        Scrape standings from selected source with optional fallback
        
        Args:
            fallback: If True, try other sources if primary fails
        
        Returns:
            Dict with group standings or None
        """
        print("=" * 60)
        print("SERIE D STANDINGS SCRAPER")
        print("=" * 60)
        
        sources = [self.source]
        
        if fallback:
            all_sources = ['flashscore', 'futebolinterior', 'ge_globo']
            sources = [s for s in all_sources if s != self.source] + sources
        
        standings = None
        
        for source in sources:
            if source == 'flashscore':
                standings = self.scrape_flashscore()
            elif source == 'futebolinterior':
                standings = self.scrape_futebolinterior()
            elif source == 'ge_globo':
                standings = self.scrape_ge_globo()
            
            if standings:
                print(f"\n✓ Using data from {source}")
                break
        
        if standings:
            # Add metadata
            standings_with_meta = {
                "phase": 1,
                "source": source,
                "last_updated": datetime.now().isoformat(),
                "groups": standings
            }
            
            # Save to file
            with open('data/standings.json', 'w', encoding='utf-8') as f:
                json.dump(standings_with_meta, f, indent=2, ensure_ascii=False)
            
            print(f"✓ Standings saved to data/standings.json")
            return standings_with_meta
        else:
            print("\n✗ Failed to scrape standings from all sources")
            return None


if __name__ == "__main__":
    # Try Flashscore first, fallback to others if needed
    scraper = SerieD_RealScraper(source='flashscore')
    standings = scraper.scrape(fallback=True)
    
    if standings:
        print(f"\n✓ Successfully retrieved {len(standings['groups'])} groups")
    else:
        print("\n✗ Unable to scrape standings")
