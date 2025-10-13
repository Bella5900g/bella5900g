#!/usr/bin/env python3
"""
Script para atualizar automaticamente o perfil do GitHub
"""

import json
import os
from datetime import datetime

def load_config():
    """Carrega a configuração do perfil"""
    with open('profile-config.json', 'r', encoding='utf-8') as f:
        return json.load(f)

def update_readme():
    """Atualiza o README.md com informações atualizadas"""
    config = load_config()
    
    # Template do README
    readme_template = f"""# 👋 Olá! Eu sou a {config['name']}

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=10B981&center=true&vCenter=true&width=435&lines=QA+Chapter+Lead+%7C+Meta;Automa%C3%A7%C3%A3o+%26+Performance;%2B10+anos+de+experi%C3%AAncia;ISTQB+CTFL+%7C+ASTFCT" alt="Typing SVG" />
</div>

<br>

<div align="center">
  <img src="https://img.shields.io/badge/QA%20Chapter%20Lead-Meta-blue?style=for-the-badge&logo=meta" alt="Meta QA Chapter Lead">
  <img src="https://img.shields.io/badge/ISTQB%20CTFL-Certified-green?style=for-the-badge&logo=testing-library" alt="ISTQB CTFL">
  <img src="https://img.shields.io/badge/ASTFCT-Advanced-orange?style=for-the-badge&logo=testing-library" alt="ASTFCT Advanced">
  <img src="https://img.shields.io/badge/10%2B%20Anos-Experi%C3%AAncia-purple?style=for-the-badge&logo=clock" alt="10+ Anos">
</div>

<br>

## 🎯 **Sobre Mim**

{config['bio']}

### 🏆 **Principais Conquistas**
- 🎯 **70%** de redução de bugs em produção
- 💰 **R$ 1.5M** em economia gerada
- ⚡ **30%** de aceleração nos releases
- 💳 **R$ 2B** em transações processadas anualmente
- 🏅 **99.9%** de uptime garantido

## 🛠️ **Tecnologias & Ferramentas**

### **Automação de Testes**
{generate_badges(config['technologies']['automation'])}

### **Ferramentas de QA**
{generate_badges(config['technologies']['qa_tools'])}

### **Desenvolvimento & Banco de Dados**
{generate_badges(config['technologies']['development'])}

### **Metodologias**
{generate_badges(config['technologies']['methodologies'])}

## 📊 **Estatísticas GitHub**

<div align="center">
  <img height="180em" src="https://github-readme-stats.vercel.app/api?username={config['username']}&show_icons=true&theme={config['theme']}&hide_border=true&count_private=true&include_all_commits=true"/>
  <img height="180em" src="https://github-readme-stats.vercel.app/api/top-langs/?username={config['username']}&layout=compact&theme={config['theme']}&hide_border=true&langs_count=8"/>
</div>

<div align="center">
  <img src="https://github-readme-streak-stats.herokuapp.com/?user={config['username']}&theme={config['theme']}&hide_border=true" alt="GitHub Streak" />
</div>

## 🎓 **Formação Acadêmica**

{generate_education(config['education'])}

## 🏆 **Certificações**

{generate_certifications(config['certifications'])}

## 📱 **Contato & Links**

<div align="center">
  <a href="{config['portfolio']}">
    <img src="https://img.shields.io/badge/Portfolio-10B981?style=for-the-badge&logo=portfolio&logoColor=white" alt="Portfolio">
  </a>
  <a href="{config['linkedin']}">
    <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=for-the-badge&logo=linkedin&logoColor=white" alt="LinkedIn">
  </a>
  <a href="mailto:{config['email']}">
    <img src="https://img.shields.io/badge/Email-D14836?style=for-the-badge&logo=gmail&logoColor=white" alt="Email">
  </a>
</div>

<br>

<div align="center">
  <img src="https://komarev.com/ghpvc/?username={config['username']}&color=blueviolet&style=flat-square" alt="Profile Views">
</div>

## 🐍 **Contribuições**

<div align="center">
  <img src="https://github.com/{config['username']}/{config['username']}/blob/output/github-contribution-grid-snake.svg" alt="Snake animation" />
</div>

---

<div align="center">
  <i>💡 "Transformando qualidade em resultados mensuráveis"</i>
</div>

<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer" />
</div>

<!-- Última atualização: {datetime.now().strftime('%d/%m/%Y %H:%M:%S')} -->
"""

    # Salva o README
    with open('README.md', 'w', encoding='utf-8') as f:
        f.write(readme_template)

def generate_badges(technologies):
    """Gera badges para as tecnologias"""
    badge_map = {
        'Selenium': '43B02A',
        'Cypress': '17202C',
        'Robot Framework': '000000',
        'Python': '3776AB',
        'JavaScript': 'F7DF1E',
        'Postman': 'FF6C37',
        'JMeter': 'D22128',
        'Azure DevOps': '0078D4',
        'Jira': '0052CC',
        'DBeaver': '372923',
        'HTML5': 'E34F26',
        'CSS3': '1572B6',
        'MySQL': '4479A1',
        'C#': '239120',
        'VS Code': '007ACC',
        'Agile': '009639',
        'DevOps': '2496ED',
        'CI/CD': '2088FF',
        'BDD': '4479A1'
    }
    
    badges = []
    for tech in technologies:
        color = badge_map.get(tech, '000000')
        badges.append(f'![{tech}](https://img.shields.io/badge/{tech.replace(" ", "%20")}-{color}?style=flat-square&logo={tech.lower().replace(" ", "-")}&logoColor=white)')
    
    return '\n'.join(badges)

def generate_education(education):
    """Gera a seção de educação"""
    edu_text = []
    for edu in education:
        status_icon = "🎓" if edu['status'] == 'Concluída' else "🌱"
        edu_text.append(f"- {status_icon} **{edu['degree']}** - {edu['institution']} ({edu['status']})")
    
    return '\n'.join(edu_text)

def generate_certifications(certifications):
    """Gera a seção de certificações"""
    cert_text = []
    for cert in certifications:
        cert_text.append(f"- 🏅 **{cert}**")
    
    return '\n'.join(cert_text)

if __name__ == "__main__":
    update_readme()
    print("✅ Perfil atualizado com sucesso!")
