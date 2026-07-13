document.getElementById('generateBtn').addEventListener('click', async () => {
    const patentText = document.getElementById('patentInput').value;
    if (!patentText) {
        alert('Please enter your patent requirements.');
        return;
    }

    const btn = document.getElementById('generateBtn');
    const btnText = btn.querySelector('.btn-text');
    const loader = btn.querySelector('.loader');
    const resultsSection = document.getElementById('resultsSection');
    
    // UI Loading State
    btnText.classList.add('hidden');
    loader.classList.remove('hidden');
    btn.disabled = true;
    resultsSection.classList.remove('visible');
    
    setTimeout(() => {
        resultsSection.classList.remove('hidden');
    }, 300); // slight delay to allow display:block before opacity transition

    try {
        const response = await fetch('/api/generate', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({ patent_text: patentText })
        });

        const data = await response.json();

        if (response.ok) {
            document.getElementById('agentLogs').textContent = data.logs;
            document.getElementById('finalDocument').textContent = data.document;
            resultsSection.classList.add('visible');
            document.getElementById('downloadPdfBtn').classList.remove('hidden');
        } else {
            alert('Error: ' + data.error);
        }
    } catch (error) {
        console.error('Error generating document:', error);
        alert('Failed to connect to the Agentic AI server.');
    } finally {
        // Reset UI State
        btnText.classList.remove('hidden');
        loader.classList.add('hidden');
        btn.disabled = false;
    }
});

document.getElementById('downloadPdfBtn').addEventListener('click', () => {
    const element = document.getElementById('finalDocument');
    const opt = {
        margin:       1,
        filename:     'Patent_Application_Draft.pdf',
        image:        { type: 'jpeg', quality: 0.98 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }
    };
    html2pdf().set(opt).from(element).save();
});
