# 🚀 Script de Commit Diário - Isabella
# Execute este script todos os dias para fazer commits manuais

param(
    [string]$TipoCommit = "daily",
    [string]$Mensagem = ""
)

# Configurações
$DataAtual = Get-Date -Format "yyyy-MM-dd"
$HoraAtual = Get-Date -Format "HH:mm"
$ArquivoLog = "daily-commits.log"

# Função para fazer commit
function Fazer-Commit {
    param(
        [string]$Tipo,
        [string]$Mensagem,
        [string]$Arquivo
    )
    
    # Criar ou atualizar arquivo
    $Conteudo = "Commit $Tipo - $DataAtual $HoraAtual`n$Mensagem`n"
    Add-Content -Path $Arquivo -Value $Conteudo
    
    # Git operations
    git add $Arquivo
    git commit -m "$Tipo $Mensagem - $DataAtual"
    git push origin main
    
    Write-Host "✅ Commit realizado com sucesso!" -ForegroundColor Green
    Write-Host "📝 Tipo: $Tipo" -ForegroundColor Cyan
    Write-Host "💬 Mensagem: $Mensagem" -ForegroundColor Yellow
}

# Função para commit de documentação
function Commit-Documentacao {
    $Mensagem = "📚 docs: Update documentation with latest information"
    Fazer-Commit -Tipo "📚" -Mensagem "Update documentation - $DataAtual" -Arquivo "docs/updates.md"
}

# Função para commit de melhoria
function Commit-Melhoria {
    $Mensagem = "🔧 refactor: Improve code structure and organization"
    Fazer-Commit -Tipo "🔧" -Mensagem "Code improvements - $DataAtual" -Arquivo "improvements.md"
}

# Função para commit de funcionalidade
function Commit-Funcionalidade {
    $Mensagem = "✨ feat: Add new feature or enhancement"
    Fazer-Commit -Tipo "✨" -Mensagem "New feature - $DataAtual" -Arquivo "features.md"
}

# Função para commit de correção
function Commit-Correcao {
    $Mensagem = "🐛 fix: Fix minor issues and improvements"
    Fazer-Commit -Tipo "🐛" -Mensagem "Bug fixes - $DataAtual" -Arquivo "fixes.md"
}

# Função para commit personalizado
function Commit-Personalizado {
    param([string]$MensagemPersonalizada)
    
    if ([string]::IsNullOrEmpty($MensagemPersonalizada)) {
        $MensagemPersonalizada = "Custom update - $DataAtual"
    }
    
    Fazer-Commit -Tipo "📝" -Mensagem $MensagemPersonalizada -Arquivo "custom-updates.md"
}

# Menu principal
function Mostrar-Menu {
    Write-Host "🚀 Sistema de Commits Diários - Isabella" -ForegroundColor Magenta
    Write-Host "=========================================" -ForegroundColor Magenta
    Write-Host ""
    Write-Host "📅 Data: $DataAtual" -ForegroundColor Cyan
    Write-Host "🕐 Hora: $HoraAtual" -ForegroundColor Cyan
    Write-Host ""
    Write-Host "Escolha o tipo de commit:" -ForegroundColor Yellow
    Write-Host "1. 📚 Documentação" -ForegroundColor Green
    Write-Host "2. 🔧 Melhoria" -ForegroundColor Blue
    Write-Host "3. ✨ Funcionalidade" -ForegroundColor Magenta
    Write-Host "4. 🐛 Correção" -ForegroundColor Red
    Write-Host "5. 📝 Personalizado" -ForegroundColor Yellow
    Write-Host "6. 🚀 Commit Rápido" -ForegroundColor Cyan
    Write-Host "0. ❌ Sair" -ForegroundColor Gray
    Write-Host ""
}

# Função para commit rápido
function Commit-Rapido {
    $Mensagem = "📅 Daily activity - $DataAtual"
    Fazer-Commit -Tipo "📅" -Mensagem "Daily activity - $DataAtual" -Arquivo $ArquivoLog
}

# Execução principal
if ($TipoCommit -eq "daily" -and [string]::IsNullOrEmpty($Mensagem)) {
    # Modo interativo
    do {
        Mostrar-Menu
        $Escolha = Read-Host "Digite sua escolha (0-6)"
        
        switch ($Escolha) {
            "1" { Commit-Documentacao }
            "2" { Commit-Melhoria }
            "3" { Commit-Funcionalidade }
            "4" { Commit-Correcao }
            "5" { 
                $MensagemPersonalizada = Read-Host "Digite sua mensagem personalizada"
                Commit-Personalizado -MensagemPersonalizada $MensagemPersonalizada
            }
            "6" { Commit-Rapido }
            "0" { 
                Write-Host "👋 Até logo!" -ForegroundColor Green
                break
            }
            default { 
                Write-Host "❌ Opção inválida!" -ForegroundColor Red
            }
        }
        
        if ($Escolha -ne "0") {
            Write-Host ""
            Write-Host "Pressione qualquer tecla para continuar..." -ForegroundColor Gray
            $null = $Host.UI.RawUI.ReadKey("NoEcho,IncludeKeyDown")
            Write-Host ""
        }
    } while ($Escolha -ne "0")
} else {
    # Modo automático
    switch ($TipoCommit.ToLower()) {
        "docs" { Commit-Documentacao }
        "refactor" { Commit-Melhoria }
        "feat" { Commit-Funcionalidade }
        "fix" { Commit-Correcao }
        "daily" { Commit-Rapido }
        default { 
            if (-not [string]::IsNullOrEmpty($Mensagem)) {
                Commit-Personalizado -MensagemPersonalizada $Mensagem
            } else {
                Commit-Rapido
            }
        }
    }
}

Write-Host ""
Write-Host "🎯 Próximos passos:" -ForegroundColor Yellow
Write-Host "1. Verifique seu GitHub em 24h" -ForegroundColor Cyan
Write-Host "2. Execute este script diariamente" -ForegroundColor Cyan
Write-Host "3. Mantenha consistência" -ForegroundColor Cyan
Write-Host ""
Write-Host "📊 Para executar automaticamente:" -ForegroundColor Magenta
Write-Host ".\daily-commit-script.ps1 -TipoCommit daily" -ForegroundColor Gray
Write-Host ".\daily-commit-script.ps1 -TipoCommit docs" -ForegroundColor Gray
Write-Host ".\daily-commit-script.ps1 -Mensagem 'Sua mensagem aqui'" -ForegroundColor Gray
