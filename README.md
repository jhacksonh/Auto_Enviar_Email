# Auto_Enviar_Email
## projeto simples para enviar Email para multiplas pessoas ao mesmo tempo.

### Passo a passo de como gerar a Senha de APP, para usar o sistema*
1. **Acesse sua conta Google**
   - Vá para [https://myaccount.google.com](https://myaccount.google.com).
   - Faça login com seu e-mail e senha.(Que deseja usar para envio).

2. **Ative a verificação em duas etapas**
   - Clique em **Segurança** no menu lateral.
   - Role até **Como fazer login no Google** e clique em **Verificação em duas etapas**.
   - Siga as instruções para ativar, como adicionar um número de telefone ou aplicativo autenticador.

3. **Gere a senha de aplicativo**
   - Após ativar a verificação em duas etapas, volte à página de **Segurança**.
   - Clique em **Senhas de aplicativo** (na mesma seção "Como fazer login no Google").
   - caso não encontre, busque na aba de pesquisa por "Senha de APP"
   - Escolha o tipo de aplicativo (ex.: "E-mail") e o dispositivo (ex.: "Computador Windows").
   - Clique em **Gerar**.

4. **Copie e use a senha**
   - Uma senha será exibida (algo como `abcd-efgh-ijkl-mnop`).
   - Copie essa senha e use-a no lugar da senha(linha 15), coloque seu email(linha 14) no código. Ou configure um .env(recomendado) com as credenciais.

5. **Teste seu envio**
   - Execute o código ou aplicativo para garantir que o envio está funcionando corretamente.
   - Não se esquece de preencher o txt com o nome(s) e email(s) de destino. Como nele está exemplificado.