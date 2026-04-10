# Python Data Collector

Projeto para coleta de dados de API pública, armazenamento em banco SQLite e execução automatizada.

## Tecnologias
- Python
- Requests
- SQLite

## Funcionalidades
- Consumo de API REST
- Armazenamento em banco de dados
- Prevenção de duplicidade
- Estrutura modular (service, database)

## Como rodar
```bash
pip install -r requirements.txt

python main.py collect
python main.py list
python main.py clear
