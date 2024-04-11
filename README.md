<p class="header" align="center">
 <img width="350px" src="./assets/logo.png" align="center" alt="InfoSecTools" />
 <h2 align="center">InfoSecTools</h2>
 <p align="center">Realize a instalação de suas ferramentas de segurança da informação de forma automatizada!</p>
</p>
<p align="center">
  <a href="https://github.com/guiaanonima/InfoSecTools/graphs/contributors">
    <img alt="GitHub Contributors" src="https://img.shields.io/github/contributors/guiaanonima/InfoSecTools?color=0088ff" />
  </a>
  <a href="https://github.com/guiaanonima/InfoSecTools/issues">
    <img alt="Issues" src="https://img.shields.io/github/issues/guiaanonima/InfoSecTools?color=0088ff" />
  </a>
  <a href="https://github.com/guiaanonima/InfoSecTools/pulls">
    <img alt="GitHub pull requests" src="https://img.shields.io/github/issues-pr/guiaanonima/InfoSecTools?color=0088ff" />
  </a>
  <a href="https://discord.guiaanonima.com/">
    <img src="https://img.shields.io/discord/719674366861770834?color=0088ff&label=discord">
  </a>
  <br />
  <br />
</p>
<p class="links" align="center">
  <a href="#execução-do-programa">Ver exemplos</a>
  .
  <a href="https://github.com/guiaanonima/InfoSecTools/issues/new?template=feature.yaml"">Solicitar recursos</a>
  .
  <a href="https://github.com/guiaanonima/InfoSecTools/issues/new?template=feature.yaml">Reportar bugs</a>
  .
  <a href="https://github.com/guiaanonima/InfoSecTools/blob/main/CONTRIBUTING.md">Quero contribuir</a>
</p>
 <br />

# Como utilizar?
Essa ferramenta, escrita em Python, visa facilitar a instalação e configuração de diversas ferramentas de cybersecurity, de diversos repositórios. Você pode escolher quais tipos de ferramentas você deseja realizar a instalação.

## Pré-requisitos
- Uma máquina rodando uma distribuição Linux compatível.
- Direitos de superusuário (root) para instalação de pacotes.
- Python 3.x instalado.
- Conexão estável com a internet.

> [!IMPORTANT]\
> Não possuímos compatibilidade com Windows, apenas com distribuições Linux. Nestas, utilizamos apenas o gerenciador de pacote `apt`, no momento. Caso a sua distribuição linux não possua esse gerenciador, por favor, [solicite](https://github.com/guiaanonima/InfoSecTools/issues/new?template=feature.yaml) para ser incluído na ferramenta.\
> É recomendado o uso desta ferramenta em uma VM (Virtual Machine), devido a instalação de diversas dependências.

Distribuição | Testada |
-- |-- |
Ubuntu 22.04 LTS | ✓
Debian 12.04 | ✓
Kali (2023.4) | ✓
Arch | ✗

## Instalação

1. Realize o login como usuário root
```shell
su
```
2. Realiza o clone do repositório

```shell
git clone https://github.com/guiaanonima/InfoSecTools.git
```
3. Entre no diretório do repositório:
```shell
cd ./InfoSecTools
```

> [!TIP]
> Sugestão: Recomendamos realizar a instalação das dependências em um ambiente isolado, como, por exemplo, utilizando o [virtualenv](https://virtualenv.pypa.io/en/latest/) ou [conda](https://docs.conda.io/en/latest/)!
4. Instale as dependências para poder executar o código Python:

```shell
pip install -r requirements.txt
```

![](/assets/gif/instalacao.gif)

## Execução do programa
Para executar o programa, execute o comando abaixo:
```shell
python3 main.py
```

![](/assets/gif/execucao.gif)

# Contribua!
Contribuições são bem-vindas! Se você deseja adicionar uma ferramenta, corrigir um bug ou melhorar a documentação, sinta-se à vontade para abrir uma issue e/ou fazer um pull request.
