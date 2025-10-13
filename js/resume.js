// JavaScript para funcionalidade do currículo
document.addEventListener('DOMContentLoaded', function() {
    // Adicionar funcionalidade de download do currículo
    const resumeLink = document.querySelector('a[href="assets/resume.html"]');
    
    if (resumeLink) {
        resumeLink.addEventListener('click', function(e) {
            e.preventDefault();
            
            // Abrir o currículo em nova aba
            const newWindow = window.open('assets/resume.html', '_blank');
            
            // Focar na nova janela
            if (newWindow) {
                newWindow.focus();
            }
        });
    }
    
    // Adicionar funcionalidade de impressão/PDF
    function setupResumePrint() {
        const resumeWindow = window.open('assets/resume.html', '_blank');
        
        if (resumeWindow) {
            resumeWindow.addEventListener('load', function() {
                // Aguardar um pouco para garantir que o conteúdo carregou
                setTimeout(() => {
                    resumeWindow.print();
                }, 1000);
            });
        }
    }
    
    // Expor função globalmente para uso no currículo
    window.setupResumePrint = setupResumePrint;
});

// Função para gerar PDF usando jsPDF (opcional)
function generatePDFWithJsPDF() {
    // Esta função pode ser implementada se você quiser usar jsPDF
    // Por enquanto, usamos a funcionalidade nativa de impressão do navegador
    
    const resumeWindow = window.open('assets/resume.html', '_blank');
    
    if (resumeWindow) {
        resumeWindow.addEventListener('load', function() {
            setTimeout(() => {
                resumeWindow.print();
            }, 1000);
        });
    }
}

// Função para download direto (se necessário)
function downloadResume() {
    // Criar um link temporário para download
    const link = document.createElement('a');
    link.href = 'assets/resume.html';
    link.download = 'Isabella_Vieira_Barbosa_Curriculo.html';
    document.body.appendChild(link);
    link.click();
    document.body.removeChild(link);
}

// Adicionar evento de teclado para facilitar o download
document.addEventListener('keydown', function(e) {
    // Ctrl + D para download do currículo
    if (e.ctrlKey && e.key === 'd') {
        e.preventDefault();
        const resumeLink = document.querySelector('a[href="assets/resume.html"]');
        if (resumeLink) {
            resumeLink.click();
        }
    }
});

// Função para compartilhar currículo
function shareResume() {
    if (navigator.share) {
        navigator.share({
            title: 'Currículo - Isabella Vieira Barbosa',
            text: 'QA Chapter Lead | Meta | Automação & Performance',
            url: window.location.origin + '/assets/resume.html'
        });
    } else {
        // Fallback: copiar URL para clipboard
        const url = window.location.origin + '/assets/resume.html';
        navigator.clipboard.writeText(url).then(() => {
            alert('Link do currículo copiado para a área de transferência!');
        });
    }
}

// Adicionar tooltip informativo
function addResumeTooltip() {
    const resumeLink = document.querySelector('a[href="assets/resume.html"]');
    
    if (resumeLink) {
        resumeLink.title = 'Clique para visualizar e imprimir o currículo em PDF';
        
        // Adicionar evento de hover para mostrar mais informações
        resumeLink.addEventListener('mouseenter', function() {
            this.style.transform = 'scale(1.05)';
        });
        
        resumeLink.addEventListener('mouseleave', function() {
            this.style.transform = 'scale(1)';
        });
    }
}

// Inicializar tooltip quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', addResumeTooltip);
