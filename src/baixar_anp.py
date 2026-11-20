import requests
import pathlib

URL = "https://www.gov.br/anp/pt-br/centrais-de-conteudo/dados-abertos/arquivos/shpc/dsas/ca/ca-2026-01.zip"
DESTINO = "data/anp/zip"

def baixar(url: str, pasta: str) -> None:
    pathlib.Path(pasta).mkdir(parents=True, exist_ok=True) #verifica se a pasta já existe
    resp = requests.get(url, stream=True, timeout=60)

    resp.raise_for_status()
    arquivo = pathlib.Path(pasta) / pathlib.Path(url).name

    with open(arquivo, "wb") as f:
        for pedaco in resp.iter_content(chunk_size=1024 * 1024):
            f.write(pedaco)

    print(f"salvo em {arquivo}")

if __name__ == "__main__":
    baixar(URL, DESTINO)