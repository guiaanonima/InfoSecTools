categorias = {
	1: ['Coleta de Informações', ['kali-tools-information-gathering']],
	2: ['Análise de Vulnerabilidade', ['kali-tools-vulnerability']],
	3: ['Ataques Wireless', ['kali-tools-wireless']],
	4: ['Aplicações Web', ['kali-tools-web']],
	5: ['Sniffing e Spoofing', ['kali-tools-sniffing-spoofing']],
	7: ['Ferramentas de Relatório', ['kali-tools-reporting']],
	8: ['Ferramentas de Exploração', ['kali-tools-exploitation']],
	9: ['Ferramentas Forenses', ['kali-tools-forensics']],
	10: ['Teste de Estresse', ['dhcpig', 'funkload', 'iaxflood', 'inviteflood', 'ipv6-toolkit', 'mdk3', 'reaver', 'rtpflood', 'slowhttptest', 't50', 'termineter', 'thc-ipv6', 'thc-ssl-dos']],
	11: ['Ataques de Senha', ['kali-tools-passwords']],
	12: ['Engenharia Reversa', ['kali-tools-reverse-engineering']],
	13: ['Hacking de Hardware', ['kali-tools-hardware']],
    14: ['Ferramentas de Pós Exploração', ['kali-tools-post-exploitation']],
}

categorias[15] = ['Todas as Ferramentas', [ferramenta for ferramentas in categorias.values() for ferramenta in ferramentas[1]]] # Adicição de todas as ferramentas para opção de instalação
