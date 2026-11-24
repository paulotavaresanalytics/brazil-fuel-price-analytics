import re

from pyspark.sql import SparkSession

PASTA_CSV = "data/anp/csv"
SAIDA_RAW = "saida/raw/anp"

def normalizar_colunas(df):
    novos_nomes = [re.sub(r"[^0-9a-zA-Z]+", "_", c).strip("_").lower() for c in df.columns]
    return df.toDF(*novos_nomes)


def main() -> None:
    spark = SparkSession.builder.master("local[*]").appName("raw_anp").getOrCreate()
    df = spark.read.csv(PASTA_CSV, header=True, sep=";")
    df = normalizar_colunas(df)
    df.write.mode("overwrite").parquet(SAIDA_RAW)
    df.printSchema()
    print(df.count())
    spark.stop()


if __name__ == "__main__":
    main()
