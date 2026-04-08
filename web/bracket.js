// Load and display bracket data

async function loadBracket() {
    try {
        const response = await fetch('../data/bracket.json');
        const bracket = await response.json();
        renderBracket(bracket);
    } catch (error) {
        console.error('Error loading bracket:', error);
        document.getElementById('bracket').innerHTML = 
            '<p style="color: red;">Erro ao carregar dados do bracket</p>';
    }
}

function renderBracket(bracket) {
    const container = document.getElementById('bracket');
    container.innerHTML = '';
    
    // Phase 1 - Group Standings
    const phase1Div = createPhaseSection('Fase 1', bracket.phase_1);
    container.appendChild(phase1Div);
    
    // Phase 2 - First elimination round
    if (bracket.phase_2.length > 0) {
        const phase2Div = createPhaseSection('Fase 2', bracket.phase_2);
        container.appendChild(phase2Div);
    }
    
    // Add other phases...
    
    updateLastModified();
}

function createPhaseSection(phaseName, data) {
    const section = document.createElement('div');
    section.className = 'phase';
    
    const title = document.createElement('h3');
    title.textContent = phaseName;
    section.appendChild(title);
    
    // Add match boxes for this phase
    // Implementation depends on data structure
    
    return section;
}

function updateLastModified() {
    const now = new Date();
    const timeStr = now.toLocaleTimeString('pt-BR');
    document.getElementById('lastUpdate').textContent = 
        `Última atualização: ${timeStr}`;
}

// Load bracket on page load
document.addEventListener('DOMContentLoaded', loadBracket);
