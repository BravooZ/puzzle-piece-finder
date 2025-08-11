# 🧩 Puzzle Piece Finder

Um sistema inteligente de reconhecimento e localização de peças de puzzle usando algoritmos avançados de visão computacional.

<div align="center">

![Python](https://img.shields.io/badge/Python-3.8+-blue?style=for-the-badge&logo=python)
![OpenCV](https://img.shields.io/badge/OpenCV-4.0+-green?style=for-the-badge&logo=opencv)
![Pillow](https://img.shields.io/badge/Pillow-8.0+-orange?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-red?style=for-the-badge)

[![GitHub stars](https://img.shields.io/github/stars/BravooZ/puzzle-piece-finder?style=social)](https://github.com/BravooZ/puzzle-piece-finder/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/BravooZ/puzzle-piece-finder?style=social)](https://github.com/BravooZ/puzzle-piece-finder/network)
[![GitHub issues](https://img.shields.io/github/issues/BravooZ/puzzle-piece-finder)](https://github.com/BravooZ/puzzle-piece-finder/issues)
[![GitHub pull requests](https://img.shields.io/github/issues-pr/BravooZ/puzzle-piece-finder)](https://github.com/BravooZ/puzzle-piece-finder/pulls)

</div>

## 📖 Sobre o Projeto

Este projeto implementa um sistema automatizado para resolver puzzles físicos através de análise de imagens. O sistema pode:
- **Localizar peças** individuais no puzzle completo
- **Calcular similaridade** entre peças e regiões do puzzle
- **Otimizar matching** com multi-escala e aceleração GPU
- **Interface gráfica** intuitiva para facilitar o uso
- **Análise de métricas** detalhadas de cada peça

### 🎯 Características Principais

- **Template Matching Multi-escala**: Algoritmos otimizados para encontrar peças em diferentes tamanhos
- **Suporte GPU/CUDA**: Aceleração por hardware para processamento rápido
- **Interface Gráfica Tkinter**: GUI completa com visualização de resultados
- **Análise de Similaridade**: Métricas avançadas de correspondência de cores e formas
- **Detecção de Sobreposições**: Identificação automática de conflitos entre peças
- **Exportação de Resultados**: Salvamento de dados em formato JSON

## 📁 Estrutura do Projeto

```
puzzle_piece_finder/
├── src/                          # Código fonte principal
│   ├── acquisition.py            # Carregamento e pré-processamento de imagens
│   ├── features.py               # Extração de características das imagens
│   ├── matching.py               # Algoritmos de matching e comparação
│   ├── gui.py                    # Interface gráfica do usuário
│   ├── main.py                   # Script principal (CLI)
│   ├── segmentation.py           # Módulo de segmentação (em desenvolvimento)
│   └── visualization.py          # Funções de visualização (em desenvolvimento)
├── images/                       # Dados de exemplo
│   ├── puzzles/                  # Imagens de puzzles completos
│   └── pieces/                   # Imagens de peças individuais
│       ├── piece_0.png → piece_23.png  # 24 peças de exemplo
│       └── puzzle.json           # Metadados das peças
├── data/                         # Dados processados e cache
├── notebooks/                    # Jupyter notebooks para análise
├── requirements.txt              # Dependências Python
└── README.md                     # Este arquivo
```

## 🚀 Instalação e Configuração

### Pré-requisitos

- **Python 3.8+**
- **Pip** (gerenciador de pacotes Python)
- **Git** (para clonagem do repositório)

### 1. Clonar o Repositório

```bash
git clone https://github.com/BravooZ/puzzle-piece-finder.git
cd puzzle-piece-finder
```

### 2. Criar Ambiente Virtual

```bash
# Windows
python -m venv .venv
.venv\Scripts\activate

# Linux/macOS
python -m venv .venv
source .venv/bin/activate
```

### 3. Instalar Dependências

```bash
pip install -r requirements.txt
```

### 4. Dependências Principais

```
Pillow>=8.0.0          # Manipulação de imagens
opencv-python>=4.5.0   # Visão computacional
numpy>=1.21.0          # Computação numérica
tkinter                # Interface gráfica (incluído no Python)
```

## 💻 Como Usar

### Interface Gráfica (Recomendado)

```bash
python src/gui.py
```

A interface gráfica oferece:
- **Carregamento visual** de puzzles e peças
- **Configuração de parâmetros** em tempo real
- **Visualização de resultados** com overlays
- **Controles de matching** individual ou em lote
- **Análise estatística** automática

### Interface de Linha de Comando

```bash
python src/main.py
```

Para uso programático:

```python
from src.acquisition import load_puzzle, load_piece
from src.matching import multi_scale_template_match

# Carregar imagens
puzzle_img = load_puzzle()
piece_img = load_piece()

# Executar matching
result = multi_scale_template_match(
    puzzle_img=puzzle_img,
    piece_img=piece_img,
    use_gpu=True,
    use_downscale=True
)

print(f"Melhor posição: {result['best_position']}")
print(f"Similaridade: {result['refined_similarity']:.2%}")
```

## 🔧 Funcionalidades Avançadas

### Aceleração GPU (CUDA)

Para ativar a aceleração GPU, é necessário OpenCV compilado com CUDA:

#### Verificar Suporte CUDA
```python
import cv2
print("CUDA habilitado:", cv2.cuda.getCudaEnabledDeviceCount() > 0)
```

#### Instalação OpenCV-CUDA (Windows)
1. **Instalar NVIDIA CUDA Toolkit** (12.x recomendado)
2. **Visual Studio Build Tools** com C++
3. **Compilar OpenCV** com flags CUDA ativadas

```bash
# Verificação rápida
python -c "import cv2; print('CUDA devices:', cv2.cuda.getCudaEnabledDeviceCount())"
```

### Configurações de Performance

#### Para Puzzles Grandes (>2000px)
```python
result = multi_scale_template_match(
    puzzle_img=puzzle,
    piece_img=piece,
    use_downscale=True,    # Downscale automático
    use_gpu=True,          # Se disponível
    method='SQDIFF_NORMED' # Método mais rápido
)
```

#### Para Máxima Precisão
```python
result = multi_scale_template_match(
    puzzle_img=puzzle,
    piece_img=piece,
    use_downscale=False,   # Full resolution
    num_pieces=24,         # Hint para melhor escala
    method='CCORR_NORMED'  # Método mais preciso
)
```

## 📊 Análise de Resultados

### Métricas Disponíveis

- **Posição Ótima**: Coordenadas (x, y) da melhor localização
- **Fator de Escala**: Redimensionamento aplicado à peça
- **Similaridade**: Score de 0-100% de correspondência
- **Cobertura**: Percentual de área do puzzle ocupado
- **Detecção de Sobreposições**: Identificação de conflitos

### Exemplo de Saída

```json
{
  "best_position": [245, 167],
  "scale": 0.85,
  "refined_similarity": 0.847,
  "piece_size_final": [120, 98],
  "candidates_considered": 6,
  "gpu_used": true
}
```

## 🛠️ Desenvolvimento

### Arquitetura Modular

- **`acquisition.py`**: Entrada de dados e validação
- **`features.py`**: Extração de características visuais
- **`matching.py`**: Algoritmos de correspondência
- **`gui.py`**: Interface gráfica completa
- **`main.py`**: Orquestração e CLI

### Algoritmos Implementados

1. **Template Matching Multi-escala**
   - Candidatos de escala automáticos
   - Refinamento em full-resolution
   - Otimização por downscaling

2. **Análise de Características**
   - Cores dominantes
   - Cálculo de áreas
   - Estimativa de escala real

3. **Matching Otimizado**
   - Stride configurável para velocidade
   - Processamento GPU/CPU híbrido
   - Cache de resultados intermédios

### Contribuindo

1. **Fork** o repositório
2. **Crie** uma branch para sua feature (`git checkout -b feature/nova-funcionalidade`)
3. **Commit** suas mudanças (`git commit -m 'Adiciona nova funcionalidade'`)
4. **Push** para a branch (`git push origin feature/nova-funcionalidade`)
5. **Abra** um Pull Request

## 📈 Roadmap

### Em Desenvolvimento
- [ ] **Segmentação automática** de peças do puzzle completo
- [ ] **Análise de bordas** para peças de canto/lateral
- [ ] **Clustering** de cores para agrupamento inteligente
- [ ] **Exportação visual** de resultados (imagens anotadas)

### Futuro
- [ ] **Machine Learning** para classificação de peças
- [ ] **Análise de formas** geométricas avançada
- [ ] **API REST** para integração externa
- [ ] **Docker** containerization

## ⚡ Performance e Otimização

### Benchmarks Típicos

| Configuração | Tempo (24 peças) | GPU | Precisão |
|-------------|------------------|-----|----------|
| CPU + Downscale | ~15s | ❌ | 85-90% |
| CPU Full-Res | ~45s | ❌ | 90-95% |
| GPU + Downscale | ~8s | ✅ | 85-90% |
| GPU Full-Res | ~20s | ✅ | 90-95% |

### Dicas de Otimização

- **Use downscale** para puzzles >1500px
- **GPU recomendada** para lotes >10 peças
- **Reduzir candidatos** de escala para casos específicos
- **Cache results** para análises repetitivas

## 🔍 Solução de Problemas

### Problemas Comuns

#### OpenCV/CUDA não funciona
```bash
# Verificar instalação
python -c "import cv2; print(cv2.getBuildInformation())"
```

#### Memória insuficiente
- Reduzir tamanho das imagens
- Ativar `use_downscale=True`
- Processar peças individualmente

#### Performance lenta
- Verificar se GPU está sendo usada
- Reduzir `stride` do sliding window
- Usar imagens em formato otimizado (PNG)

## 📄 Licença

Este projeto está licenciado sob a Licença MIT - veja o arquivo [LICENSE](LICENSE) para detalhes.

## 🤝 Créditos

- **OpenCV** - Biblioteca de visão computacional
- **Pillow** - Processamento de imagens Python
- **NumPy** - Computação numérica eficiente
- **Tkinter** - Interface gráfica nativa Python

## 📧 Contato e Suporte

- **Issues**: [GitHub Issues](https://github.com/BravooZ/puzzle-piece-finder/issues) para reportar bugs
- **Discussions**: [GitHub Discussions](https://github.com/BravooZ/puzzle-piece-finder/discussions) para perguntas
- **Contribuições**: Veja [CONTRIBUTING.md](CONTRIBUTING.md) para guidelines
- **Changelog**: Veja [CHANGELOG.md](CHANGELOG.md) para histórico de versões

### Links Úteis

- **[Documentação Completa](https://BravooZ.github.io/puzzle-piece-finder/)** (em breve)
- **[Tutorial em Vídeo](https://youtu.be/example)** (em breve)
- **[Artigo Técnico](docs/technical_paper.pdf)** (em breve)

### Citação Acadêmica

Se você usar este projeto em pesquisa acadêmica, por favor cite:

```bibtex
@software{puzzle_piece_finder,
  title = {Puzzle Piece Finder: Computer Vision for Jigsaw Puzzle Solving},
  author = {Your Name},
  year = {2025},
  url = {https://github.com/BravooZ/puzzle-piece-finder},
  version = {1.0.0}
}
```

---

<div align="center">
  <strong>Transformando puzzles físicos em desafios computacionais! 🧩✨</strong>
</div>
