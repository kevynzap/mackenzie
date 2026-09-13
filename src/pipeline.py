import pandas as pd

def processar_vendas(path: str) -> pd.DataFrame:
    """
    processar dados de vendas
    """
    df = pd.read_csv(path)

    df['valor_total'] = df['quantidade'] * df['preco']

    vendas_agg = (
        df
        .groupby('produto')
        .agg(
            qtd_total=('quantidade', 'sum'), 
            vlt_total=('valor_total', 'sum')
        )
        .reset_index()
    )

    vendas_agg.to_csv('output/vendas_processadas.csv', index=False)

    return vendas_agg


#processar_vendas('data/vendas.csv')