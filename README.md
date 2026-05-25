
Leia, por favor!!

# Configuração do Ambiente
python -m venv venv
# Ative o ambiente virtual
.\venv\Scripts\activate
# Instale as dependências
pip install -r requirements.txt
# Execute o aplicativo
streamlit run App.py
# Variáveis de Ambiente
Certifique-se de configurar as seguintes variáveis de ambiente no arquivo `.env`:
```env
GEMINI_API_KEY="SUA_CHAVE_DE_API_GEMINI"
```
APP_URL="URL_DO_SEU_APP"

Essas variáveis são essenciais para o funcionamento do aplicativo, garantindo que ele possa se comunicar com a API do Gemini e ser acessível 
através da URL especificada.   
Certifique-se de manter essas informações seguras e não compartilhá-las publicamente.   
Após configurar as variáveis de ambiente, você pode iniciar o aplicativo usando o comando `streamlit run App.py` e acessar a interface do 
usuário através da URL configurada.   
Lembre-se de que as variáveis de ambiente são sensíveis e devem ser protegidas adequadamente, especialmente a chave de API, para evitar acesso 
não autorizado. Além disso, é recomendável adicionar o arquivo `.env` ao seu arquivo `.gitignore` para evitar que as informações sensíveis 
sejam comprometidas em repositórios públicos.
```gitignore
```
