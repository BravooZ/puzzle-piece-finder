# Contributing to Puzzle Piece Finder

Obrigado pelo interesse em contribuir para o projeto! Este guia ajudará você a começar.

## 🚀 Como Contribuir

### Reportar Bugs

1. **Verifique** se o bug já foi reportado nas [Issues](https://github.com/your-username/puzzle-piece-finder/issues)
2. **Crie uma nova issue** com:
   - Descrição clara do problema
   - Passos para reproduzir
   - Comportamento esperado vs. atual
   - Screenshots (se aplicável)
   - Versão do Python e sistema operacional

### Sugerir Melhorias

1. **Abra uma issue** com tag `enhancement`
2. **Descreva** a funcionalidade proposta
3. **Explique** por que seria útil
4. **Considere** implementações alternativas

### Contribuir com Código

1. **Fork** o repositório
2. **Clone** seu fork localmente
3. **Crie uma branch** para sua feature:
   ```bash
   git checkout -b feature/minha-nova-feature
   ```
4. **Faça suas mudanças** seguindo os padrões do projeto
5. **Teste** suas mudanças
6. **Commit** com mensagens descritivas:
   ```bash
   git commit -m "feat: adiciona detecção automática de bordas"
   ```
7. **Push** para sua branch:
   ```bash
   git push origin feature/minha-nova-feature
   ```
8. **Abra um Pull Request**

## 📝 Padrões de Código

### Style Guide
- **PEP 8** para estilo Python
- **Type hints** para funções públicas
- **Docstrings** para módulos, classes e funções
- **Comentários** em português ou inglês

### Exemplo de Função
```python
def calculate_similarity(image1: Image.Image, image2: Image.Image) -> float:
    """Calcula similaridade entre duas imagens.
    
    Args:
        image1: Primeira imagem para comparação
        image2: Segunda imagem para comparação
        
    Returns:
        float: Valor de similaridade entre 0.0 e 1.0
        
    Raises:
        ValueError: Se as imagens têm tamanhos incompatíveis
    """
    # Implementação aqui
    pass
```

### Estrutura de Commits
- `feat:` nova funcionalidade
- `fix:` correção de bug
- `docs:` alterações na documentação
- `style:` formatação, sem mudança de código
- `refactor:` refatoração sem alterar funcionalidade
- `test:` adicionar ou alterar testes
- `perf:` melhoria de performance

## 🧪 Testando

### Executar Testes Localmente
```bash
# Instalar dependências de desenvolvimento
pip install -r requirements-dev.txt

# Executar testes
python -m pytest tests/

# Com cobertura
python -m pytest --cov=src tests/
```

### Testando a GUI
- Teste todas as funcionalidades principais
- Verifique comportamento com imagens de diferentes tamanhos
- Confirme que cancelamento funciona corretamente
- Teste com e sem GPU habilitada

## 📚 Áreas que Precisam de Ajuda

### Alta Prioridade
- [ ] **Testes unitários** para módulos de matching
- [ ] **Documentação** de APIs internas
- [ ] **Otimização** de algoritmos de template matching
- [ ] **Tratamento de erros** mais robusto

### Funcionalidades Desejadas
- [ ] **Segmentação automática** de peças
- [ ] **Machine learning** para classificação
- [ ] **API REST** para integração
- [ ] **Análise de formas** geométricas

### Melhorias de UX
- [ ] **Drag & drop** de imagens na GUI
- [ ] **Preview** de resultados em tempo real
- [ ] **Configurações** persistentes
- [ ] **Internacionalização** (i18n)

## 💡 Dicas para Contribuidores

### Configuração do Ambiente
```bash
# Clone do repositório
git clone https://github.com/your-username/puzzle-piece-finder.git
cd puzzle-piece-finder

# Ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
venv\Scripts\activate     # Windows

# Instalar em modo desenvolvimento
pip install -e .
pip install -r requirements-dev.txt
```

### Debug e Performance
- Use **cProfile** para identificar bottlenecks
- **Logs detalhados** para debugging
- **Profiling de GPU** com nvidia-smi
- **Memory profiling** com memory_profiler

### Documentação
- README sempre atualizado
- **Docstrings** detalhadas
- **Exemplos** de uso práticos
- **Diagramas** para algoritmos complexos

## 🤝 Código de Conduta

- **Seja respeitoso** e inclusivo
- **Colabore** de forma construtiva
- **Mantenha** discussões focadas no projeto
- **Ajude** outros contribuidores

## 🆘 Precisa de Ajuda?

- **Issues**: Para bugs e sugestões
- **Discussions**: Para perguntas gerais
- **Email**: [manter privado por enquanto]
- **Discord/Slack**: [links quando disponíveis]

## 🎯 Roadmap de Contribuições

### Q1 2025
- [ ] Sistema de testes robusto
- [ ] Documentação API completa
- [ ] Otimizações de performance

### Q2 2025
- [ ] Machine learning básico
- [ ] API REST
- [ ] Docker deployment

### Q3+ 2025
- [ ] Mobile app
- [ ] Web interface
- [ ] Cloud processing

Obrigado por ajudar a tornar este projeto ainda melhor! 🧩✨
