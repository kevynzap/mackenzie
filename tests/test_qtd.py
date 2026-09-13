from src.pipeline import processar_vendas

def test_processar_vendas():
    resultado = processar_vendas('tests/vendas_teste.csv')

    assert resultado.loc[resultado["produto"] == "Produto A", "qtd_total"].iloc[0] == 2 

    #resultado[resultado['produto'] == 'Produto A']['vlt_total']