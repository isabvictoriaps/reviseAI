# Gerador de Flashcards Inteligentes com IA

## Descrição
Transforme seu aprendizado com facilidade! Este projeto permite a criação automática de flashcards interativos a partir de vídeos do YouTube e textos inseridos manualmente. Usamos a poderosa API Gemini para processar linguagem natural e gerar conteúdo educativo de alta qualidade. Ideal para fixar conhecimentos e revisar de forma eficiente!

---
1. **Entrada de Dados**
   - 🎥 Envio de links de vídeos do YouTube.
   - 📝 Inserção direta de textos.

### 2. Geração de Flashcards
- 📚 **Quantidade Personalizada:** O usuário define a quantidade de flashcards (entre 5 e 10).
- 🎯 **Qualidade:** Flashcards claros, objetivos e relevantes.
- ✅ **Revisão Automática:** Detecção de duplicidades e inconsistências.
- ⚙️ **Níveis de Dificuldade:** Escolha entre básico, intermediário e avançado.

### 3. Controle de Quantidade
- 🔢 **Faixa Permitida:** O usuário pode gerar de 5 a 10 flashcards por vez.
- 🚫 **Padrão Automático:** Se o valor inserido for inválido, o sistema gera 5 flashcards por padrão.

### 4. Tratamento de Erros
- 🚫 **Notificação:** Usuário recebe alertas em caso de falhas na geração.
- 🛠️ **Logs de Erro:** Registros automáticos para análise e correção.
- 💡 **Sugestões:** O sistema oferece temas alternativos em caso de erro.

### ROTAS

1. POST /flashcards/generate
   
