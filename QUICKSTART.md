# Quick Start Guide

Este guia rápido te ajudará a começar a usar o Puzzle Piece Finder em poucos minutos.

## ⚡ Instalação Rápida

```bash
# 1. Clone o repositório
git clone https://github.com/your-username/puzzle-piece-finder.git
cd puzzle-piece-finder

# 2. Crie ambiente virtual
python -m venv .venv
.venv\Scripts\activate  # Windows
# source .venv/bin/activate  # Linux/Mac

# 3. Instale dependências
pip install -r requirements.txt

# 4. Execute a GUI
python src/gui.py
```

## 🎮 Primeiro Uso

### Interface Gráfica (Recomendado)

1. **Executar GUI**: `python src/gui.py`
2. **Carregar Puzzle**: Clique em "Load Puzzle" → selecione uma imagem do puzzle completo
3. **Carregar Peças**: Clique em "Load Pieces" → selecione uma ou mais imagens de peças
4. **Executar Matching**: Clique em "Match" para uma peça ou "Match All Pieces" para todas

### Linha de Comando

```bash
# Executar CLI interativo
python src/main.py

# Siga as instruções na tela para:
# 1. Selecionar imagem do puzzle
# 2. Selecionar imagem da peça
# 3. Ver resultados do matching
```

## 📊 Interpretando Resultados

### Métricas Principais

- **Posição**: Coordenadas (x, y) onde a peça foi encontrada
- **Similaridade**: 0-100% de correspondência (>80% é muito bom)
- **Escala**: Fator de redimensionamento aplicado à peça
- **GPU**: Se aceleração por hardware foi usada

### Exemplo de Output

```
✅ Peça 1: pos=(245, 167), similaridade=87.3%, escala=0.85
```

Isso significa:
- A peça foi encontrada na posição (245, 167)
- 87.3% de confiança no matching (excelente)
- A peça foi redimensionada para 85% do tamanho original

## 🔧 Configurações Importantes

### Para Melhor Performance
- ✅ Ative "Downscale" para puzzles grandes (>1500px)
- ✅ Use "GPU" se tiver OpenCV com CUDA
- ✅ Configure "#Pieces" com o número real de peças

### Para Máxima Precisão
- ❌ Desative "Downscale" para puzzles pequenos
- ✅ Configure dimensões reais em cm
- ✅ Use imagens de alta qualidade

## 🚨 Problemas Comuns

### "GPU não disponível"
- Normal se não tiver CUDA instalado
- O sistema usa CPU automaticamente
- Performance ainda é boa para a maioria dos casos

### "Similaridade muito baixa (<50%)"
- Verifique se é a peça correta
- Tente ajustar o "#Pieces"
- Peça pode estar em escala muito diferente

### GUI trava durante matching
- Use "Cancel" para interromper
- Reduza tamanho das imagens
- Ative "Downscale"

## 📈 Próximos Passos

1. **Experimente** com suas próprias imagens de puzzle
2. **Configure GPU** seguindo o guia no README principal
3. **Explore** os exemplos em `examples/basic_usage.py`
4. **Contribua** com melhorias seguindo `CONTRIBUTING.md`

## 🆘 Precisa de Ajuda?

- **Bug ou erro**: [Abra uma issue](https://github.com/your-username/puzzle-piece-finder/issues)
- **Dúvidas**: [GitHub Discussions](https://github.com/your-username/puzzle-piece-finder/discussions)
- **Documentação completa**: Veja `README.md`

---

**Pronto! Você já pode começar a resolver puzzles com IA! 🧩✨**
