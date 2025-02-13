Passo a passo para baixar o sistema no Git Acesse o Repositório no GitHub: Abra o navegador e vá para o repositório do sistema no GitHub. Por exemplo: https://github.com/seuprojeto.

Faça o Download do ZIP:

Clique no botão verde "Code". Selecione a opção "Download ZIP". Aguarde o download ser concluído. Extraia o ZIP:

Localize o arquivo baixado (geralmente na pasta Downloads). Clique com o botão direito sobre o arquivo e selecione "Extrair Aqui" ou "Extrair para...". Verifique os Arquivos: Certifique-se de que todos os arquivos necessários foram extraídos e organizados corretamente.

Passo a passo para baixar o Docker Acesse o Site Oficial: Abra o navegador e vá para o site oficial do Docker: https://www.docker.com/.

Baixe o Docker Desktop:

Clique em "Get Docker" ou vá diretamente para a seção de downloads. Escolha a versão compatível com seu sistema operacional (Windows, Mac, ou Linux). Instale o Docker:

Abra o instalador baixado e siga as instruções da tela. No Windows, certifique-se de habilitar a opção para usar o WSL2 (subsistema Linux), se solicitado. Verifique a Instalação:

Após a instalação, abra o terminal (Prompt de Comando ou PowerShell). Digite o comando: bash Copiar código docker --version Isso mostrará a versão instalada. Configure o Docker (Opcional): Se necessário, configure o Docker para rodar em sua rede ou com permissões especiais.

Passo a passo para configurar armazenamento Linux no Windows Instale o WSL2 (Subsistema Linux no Windows):

Abra o PowerShell como administrador. Execute o comando para habilitar o WSL: bash Copiar código wsl --install Escolha uma distribuição Linux (como Ubuntu). Baixe uma Distribuição Linux:

Abra a Microsoft Store no Windows. Pesquise por Ubuntu (ou outra distribuição, como Debian). Clique em Instalar. Configure o Ambiente Linux:

Após a instalação, abra o aplicativo Ubuntu no menu Iniciar. Configure o nome de usuário e senha. Acesse o Armazenamento Compartilhado:

No Linux, o sistema de arquivos do Windows estará disponível no diretório /mnt/c/. Passo a passo para instalar Python Acesse o Site Oficial: Vá para o site oficial do Python: https://www.python.org/.

Baixe o Instalador:

Clique em Downloads. Escolha a versão recomendada para o seu sistema operacional (Windows, Mac, ou Linux). Instale o Python:

Abra o instalador baixado. Certifique-se de marcar a opção "Add Python to PATH" antes de clicar em Install Now. Verifique a Instalação:

Abra o terminal ou Prompt de Comando. Digite o comando: bash

python --version Isso mostrará a versão instalada. Instale o pip (Gerenciador de Pacotes):

No terminal, digite: bash

python -m ensurepip Resumo das Etapas Baixe o sistema no Git e extraia os arquivos. Instale o Docker para criar um ambiente de contêiner. Configure o WSL2 no Windows para rodar ferramentas Linux. Instale o Python e configure o pip para gerenciar pacotes.
