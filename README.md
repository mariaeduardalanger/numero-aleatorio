# 🕹️ Media Pipeline & 2D Game Development

Este repositório demonstra um fluxo de trabalho completo de engenharia de software: desde a **automação de processamento de ativos** até a implementação de um **jogo funcional** utilizando esses recursos.

O foco aqui foi resolver dois grandes gargalos no desenvolvimento de jogos: a padronização manual de arquivos e a gestão de caminhos em arquivos executáveis.

---

## 🛠️ Componentes do Projeto

### 1. Script de Automação de Assets (`asset_processor.py`)
Uma ferramenta CLI robusta para preparar arquivos brutos para o motor de jogo.
* **Imagens:** Redimensionamento em lote para **20x20 pixels** usando o filtro `NEAREST` para manter a fidelidade de Pixel Art.
* **Áudio:** Conversão automática de diversos formatos (`.mp3`, `.flac`) para `.wav` via integração com **FFmpeg**.
* **Resiliência:** Verificação automática de dependências de sistema antes da execução.

### 2. Catch The Hearts Game (`game.py`)
Um mini-game desenvolvido em **Pygame** focado em mecânicas de captura e progressão.
* **Dificuldade Progressiva:** Aceleração linear da velocidade dos itens para aumentar o desafio.
* **Arquitetura EXE-Ready:** Uso da função `path_recurso` para compatibilidade total com o **PyInstaller** (garante que o jogo encontre as imagens mesmo compilado).
* **Sistema de Fallback:** Se um asset falhar no carregamento, o jogo gera um substituto visual dinâmico em tempo de execução.

---

## 🚀 Como Executar

### Pré-requisitos
* Python 3.x
* [FFmpeg](https://ffmpeg.org/) configurado no sistema.

### Instalação
```bash
# Instale as dependências necessárias
pip install pygame Pillow pydub
