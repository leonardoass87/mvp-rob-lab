# Nome do arquivo: minerador_jobs.py
import feedparser
import json

class JobMiner:
    def __init__(self):
        # Feed de vagas de Python/Remoto do Freelancer.com
        self.url = "https://www.freelancer.com/rss.xml?query=python"

    def garimpar(self):
        print("🔍 ROBLab acessando Feed de Jobs (Plano B)...")
        vagas_encontradas = []
        
        try:
            feed = feedparser.parse(self.url)
            
            for entry in feed.entries:
                vagas_encontradas.append({
                    "titulo": entry.title,
                    "link": entry.link,
                    "descricao": entry.description[:200] + "..." # Resumo da vaga
                })
            
        except Exception as e:
            print(f"❌ Erro no Feed: {e}")
        
        with open("jobs.json", "w", encoding="utf-8") as f:
            json.dump(vagas_encontradas, f, indent=4, ensure_ascii=False)
        
        return len(vagas_encontradas)

if __name__ == "__main__":
    miner = JobMiner()
    qtd = miner.garimpar()
    print(f"✅ Sucesso! {qtd} vagas reais encontradas no Freelancer.com")