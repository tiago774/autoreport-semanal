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
- 
pip install pandas openpyxl schedule

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

df = pd.read_excel('dados_semanais.xlsx', sheet_name='Sheet1')

2. **Configure as credenciais de e-mail** (obrigatório):

remetente    = 'seu_email@gmail.com'
senha        = 'sua_senha_ou_app_password'
destinatario = 'equipe@empresa.com'
servidor_smtp = 'smtp.gmail.com'   # ou smtp.office365.com, smtp.mail.yahoo.com, etc.
porta        = 587

> **Atenção – Gmail / Google Workspace**  
> Não use a senha normal da conta.  
> Crie uma **Senha de aplicativo** (App Password):  
> https://myaccount.google.com/apppasswords

3. **Ajuste o agendamento** (opcional):

# Padrão: toda segunda-feira às 09:00
schedule.every().monday.at("09:00").do(gerar_relatorio_e_enviar)

# Exemplos alternativos:
# schedule.every().friday.at("17:30").do(...)
# schedule.every().day.at("08:00").do(...)          # todos os dias

## Como Executar

### Teste rápido (manual)

python main.py

Ou chame a função diretamente no código para testar:

gerar_relatorio_e_enviar()

### Modo agendado (produção)

Deixe o script rodando continuamente:

python main.py

Recomendações para manter rodando 24/7:

- **Linux/Servidor**: `nohup python main.py &` ou use `systemd`, `supervisor`, `cron + while true`
- **Windows**: Crie uma tarefa agendada no Agendador de Tarefas
- **Docker / VPS / Raspberry Pi**: Rode em container ou use `tmux` / `screen`

## Personalização Rápida – Exemplos

### Nome dinâmico do relatório

arquivo_relatorio = f'relatorio_semanal_{hoje.strftime("%Y-%m-%d")}.xlsx'

### Agregação mais completa

relatorio = df_semanal.groupby('Categoria')['Valor'].agg(
    Soma='sum',
    Média='mean',
    Contagem='count',
    Máximo='max',
    Mínimo='min'
).reset_index()

### Envio para múltiplos destinatários

destinatarios = ['joao@empresa.com', 'maria@empresa.com', 'equipe@empresa.com']
msg['To'] = ", ".join(destinatarios)
server.sendmail(remetente, destinatarios, msg.as_string())

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
