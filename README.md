Aqui está uma versão revisada, corrigida e mais polida do arquivo **README.md**, com pequenos ajustes de formatação, correção de erros de markdown (como blocos de código sem linguagem especificada), melhoria na legibilidade e adição de alguns detalhes úteis para quem for clonar o projeto no GitHub.

```markdown
# AutoReport - Geração e Envio Automático de Relatórios Semanais

Script em Python que automatiza a criação de relatórios semanais a partir de planilhas Excel.  
Ele realiza limpeza básica dos dados, filtra a semana atual, faz agregações simples, gera um arquivo Excel consolidado e envia tudo por e-mail automaticamente.

Perfeito para relatórios de vendas, indicadores de desempenho, controle de produção, atendimentos ou qualquer fluxo que dependa de planilhas atualizadas semanalmente.

## Funcionalidades

- Leitura automática de arquivos Excel
- Limpeza básica (remoção de linhas com valores nulos)
- Filtro automático dos dados da semana atual (baseado na coluna `Data`)
- Agregação por categoria (soma, média, contagem) — fácil de personalizar
- Exportação do relatório em formato `.xlsx`
- Envio automático por e-mail com anexo
- Agendamento semanal nativo (padrão: toda segunda-feira às 09:00)

## Requisitos

- Python 3.8 ou superior
- Bibliotecas Python:

```bash
pip install pandas openpyxl schedule
```

> **Nota:** `openpyxl` é necessário para ler e escrever arquivos `.xlsx`

## Estrutura Esperada da Planilha de Entrada

O script procura por um arquivo chamado **`dados_semanais.xlsx`** na mesma pasta do script.  
Colunas esperadas (case-sensitive):

| Coluna      | Tipo esperado            | Obrigatória? | Observação                                      |
|-------------|--------------------------|--------------|-------------------------------------------------|
| `Data`      | Data (dd/mm/yyyy ou ISO) | Recomendada  | Usada para filtrar apenas a semana atual       |
| `Categoria` | Texto                    | Opcional     | Ex: Produto, Setor, Equipe, Tipo de Atendimento |
| `Valor`     | Numérico                 | Opcional     | Valor a ser somado/média/etc.                   |

Se as colunas `Categoria` e `Valor` não existirem, o relatório será apenas a tabela limpa e filtrada.

## Como Configurar

1. **Ajuste o nome do arquivo de entrada** (se necessário):

```python
df = pd.read_excel('dados_semanais.xlsx', sheet_name='Sheet1')
```

2. **Configure as credenciais de e-mail** (obrigatório):

```python
remetente    = 'seu_email@gmail.com'
senha        = 'sua_senha_ou_app_password'
destinatario = 'equipe@empresa.com'
servidor_smtp = 'smtp.gmail.com'   # ou smtp.office365.com, smtp.mail.yahoo.com, etc.
porta        = 587
```

> **Atenção – Gmail / Google Workspace**  
> Não use a senha normal da conta.  
> Crie uma **Senha de aplicativo** (App Password):  
> https://myaccount.google.com/apppasswords

3. **Ajuste o agendamento** (opcional):

```python
# Padrão: toda segunda-feira às 09:00
schedule.every().monday.at("09:00").do(gerar_relatorio_e_enviar)

# Exemplos alternativos:
# schedule.every().friday.at("17:30").do(...)
# schedule.every().day.at("08:00").do(...)          # todos os dias
```

## Como Executar

### Teste rápido (manual)

```bash
python main.py
```

Ou chame a função diretamente no código para testar:

```python
gerar_relatorio_e_enviar()
```

### Modo agendado (produção)

Deixe o script rodando continuamente:

```bash
python main.py
```

Recomendações para manter rodando 24/7:

- **Linux/Servidor**: `nohup python main.py &` ou use `systemd`, `supervisor`, `cron + while true`
- **Windows**: Crie uma tarefa agendada no Agendador de Tarefas
- **Docker / VPS / Raspberry Pi**: Rode em container ou use `tmux` / `screen`

## Personalização Rápida – Exemplos

### Nome dinâmico do relatório

```python
arquivo_relatorio = f'relatorio_semanal_{hoje.strftime("%Y-%m-%d")}.xlsx'
```

### Agregação mais completa

```python
relatorio = df_semanal.groupby('Categoria')['Valor'].agg(
    Soma='sum',
    Média='mean',
    Contagem='count',
    Máximo='max',
    Mínimo='min'
).reset_index()
```

### Envio para múltiplos destinatários

```python
destinatarios = ['joao@empresa.com', 'maria@empresa.com', 'equipe@empresa.com']
msg['To'] = ", ".join(destinatarios)
server.sendmail(remetente, destinatarios, msg.as_string())
```

## Próximas Melhorias Sugeridas

- [ ] Suporte a múltiplas abas ou arquivos de entrada
- [ ] Envio do relatório em HTML (tabela + gráficos simples)
- [ ] Notificação por WhatsApp/Telegram/Slack em caso de erro
- [ ] Uso de variáveis de ambiente ou arquivo `.env` para credenciais
- [ ] Log de execução (arquivo ou console mais detalhado)
- [ ] Validação mais rigorosa das colunas obrigatórias

## Licença

[MIT License](LICENSE)

Feito com ♥ por quem cansou de gerar relatório manualmente toda segunda-feira.

Boas automações!
```

### Dicas finais para o GitHub

- Nome do arquivo: `README.md` (obrigatoriamente maiúsculo assim)
- Salve na raiz do repositório
- Se o script principal se chamar `main.py`, `autoreport.py` ou outro nome, ajuste as instruções de execução no README para refletir o nome real do arquivo.

Se quiser adicionar badges (Python version, license, etc.) ou uma seção "Como contribuir", posso incluir também. Boa sorte com o repositório, Tiago!
