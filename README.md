# PASSO A PASSO:

Você pode configurar a sua chave de API do Gemini num arquivo .env, contudo deve tomar cuidado com o compartilhamento dela. 
Para fazer o código se conectar corretamente ao banco de dados, inclua o nome do db em 'DB_PATH' no arquivo app.py OU inclua o caminho completo do db utilizando a seguinte formatação: r"caminho do db".

DB_PATH é a variável que será usada no código para representar o caminho do db no processo de conexão.
Lembre de deixar a conexão para somente leitura.

- **Criação do Ambiente virtual**  
`python -m venv venv`

- **Ative o ambiente virtual**  
`.\venv\Scripts\activate`

- **Instale as dependências**  
`pip install -r requirements.txt`

- **Execute o aplicativo**  
`streamlit run App.py`

- **Desativando o venv**  
Execute `deactivate`, mas na próxima execução terá que instalar os 'requirements' novamente.

"Lembre-se de que as variáveis de ambiente são sensíveis e devem ser protegidas adequadamente, especialmente a chave de API, para evitar acesso não autorizado. Além disso, é recomendável adicionar o arquivo `.env` ao seu arquivo `.gitignore` para evitar que as informações sensíveis sejam comprometidas em repositórios públicos."

