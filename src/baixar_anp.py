import requests
import pathlib
import zipfile

URL = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-2026-01.zip"
DESTINO = "data/anp/zip"
PASTA_CSV = "data/anp/csv"

def baixar(url: str, pasta: str) -> None:
    pathlib.Path(pasta).mkdir(parents=True, exist_ok=True)
    arquivo = pathlib.Path(pasta) / pathlib.Path(url).name

    if arquivo.exists():
        print(f"já existe: {arquivo}")
        return

    resp = requests.get(url, stream=True, timeout=60)
    resp.raise_for_status()

    with open(arquivo, "wb") as f:
        for pedaco in resp.iter_content(chunk_size=1024 * 1024):
            f.write(pedaco)

    print(f"salvo em {arquivo}")

def extrair(zip_path, pasta_csv: str) -> None:
    pathlib.Path(pasta_csv).mkdir(parents=True, exist_ok=True)

    with zipfile.ZipFile(zip_path) as z:
        z.extractall(pasta_csv)
        print(f"extraído em {pasta_csv}: {z.namelist()}")

if __name__ == "__main__":
    baixar(URL, DESTINO)

extrair(pathlib.Path(DESTINO) / pathlib.Path(URL).name, PASTA_CSV)