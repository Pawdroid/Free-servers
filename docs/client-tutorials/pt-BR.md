# Guias de configuração dos clientes

Escolha primeiro o cliente e verifique o formato de entrada. Os links do GitHub e da Cloudflare deste projeto fornecem, para cada idioma, a mesma assinatura comum de nós URI/Base64; não são perfis completos de Clash/Mihomo YAML nem perfis nativos de sing-box JSON.

Mantenha URLs de assinaturas privadas e credenciais no seu próprio dispositivo. Não as envie a sites públicos de conversão. Se precisar de outro formato, obtenha um perfil compatível com o seu provedor ou prepare-o localmente usando a documentação oficial de configuração do cliente de destino.

[v2rayN](#v2rayn)
[Clash Verge Rev](#clash-verge-rev)
[Hiddify](#hiddify)
[Clash Party](#clash-party)
[FlClash](#flclash)
[Karing](#karing)
[Throne](#throne)
[Surge Mac](#surge)
[Quantumult X](#quantumult-x)
[sing-box for Apple platforms](#sing-box)
[v2rayNG](#v2rayng)
[Clash Meta for Android](#clash-meta-android)
[Surfboard](#surfboard)
[NekoBox for Android](#nekobox-android)
[Shadowrocket](#shadowrocket)
[Stash](#stash)
[Loon](#loon)
[Egern](#egern)
[Streisand](#streisand)
[Potatso](#potatso)
[OpenClash](#openclash)
[PassWall2 / PassWall](#passwall)
[Nikki](#nikki)
[HomeProxy](#homeproxy)

<a id="v2rayn"></a>

## v2rayN

**Formato de importação:** URI / Base64

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Formato de importação:** Clash / Mihomo YAML

### Configuração rápida

1. Obtenha um perfil YAML completo compatível com Clash/Mihomo. Importe-o como perfil local ou remoto, atualize-o e selecione-o. A assinatura comum indicada acima não é um perfil YAML completo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Formato de importação:** URI / Base64 · Clash YAML · sing-box JSON

Este cliente lê vários formatos, mas use a importação comum URI/Base64 para a assinatura deste projeto. Os perfis JSON e YAML nativos continuam tendo seus próprios requisitos.

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Formato de importação:** Clash / Mihomo YAML

### Configuração rápida

1. Obtenha um perfil YAML completo compatível com Clash/Mihomo. Importe-o como perfil local ou remoto, atualize-o e selecione-o. A assinatura comum indicada acima não é um perfil YAML completo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Formato de importação:** Clash / Mihomo YAML

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Obtenha um perfil YAML completo compatível com Clash/Mihomo. Importe-o como perfil local ou remoto, atualize-o e selecione-o. A assinatura comum indicada acima não é um perfil YAML completo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Formato de importação:** URI / Base64 · Clash YAML · sing-box JSON

Este cliente lê vários formatos, mas use a importação comum URI/Base64 para a assinatura deste projeto. Os perfis JSON e YAML nativos continuam tendo seus próprios requisitos.

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Formato de importação:** URI / Base64 · sing-box JSON · Clash YAML proxies

A importação de assinaturas extrai os nós compatíveis; não presuma que as regras e outras configurações do perfil original sejam preservadas.

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Formato de importação:** Surge INI / Managed Profile

Use uma configuração do Surge ou uma URL de configuração gerenciada. Não trate uma assinatura V2Ray genérica como uma configuração completa do Surge.

### Configuração rápida

1. Obtenha um perfil completo no formato indicado acima. Importe o arquivo local ou a URL do perfil remoto compatível com este cliente, atualize-o e selecione esse perfil. Não presuma que assinaturas comuns de nós e configurações de outros aplicativos sejam intercambiáveis.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Formato de importação:** Quantumult X / server_remote

O Quantumult X usa sua própria configuração e recursos de servidores remotos; uma configuração completa e um recurso de nós são entradas diferentes.

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Obtenha um perfil completo no formato indicado acima. Importe o arquivo local ou a URL do perfil remoto compatível com este cliente, atualize-o e selecione esse perfil. Não presuma que assinaturas comuns de nós e configurações de outros aplicativos sejam intercambiáveis.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Formato de importação:** sing-box JSON

### Configuração rápida

1. Obtenha um perfil sing-box JSON completo compatível com a versão do núcleo do cliente. Adicione-o como perfil local ou remoto e atualize-o. Uma lista de URLs de nós ou um arquivo YAML do Clash não pode ser usado como sing-box JSON nativo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Formato de importação:** URI / Base64

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Formato de importação:** Clash / Mihomo YAML

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Obtenha um perfil YAML completo compatível com Clash/Mihomo. Importe-o como perfil local ou remoto, atualize-o e selecione-o. A assinatura comum indicada acima não é um perfil YAML completo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Referência técnica [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Formato de importação:** Surfboard / Surge profile

Use uma configuração do Surge ou uma URL de configuração gerenciada. Não trate uma assinatura V2Ray genérica como uma configuração completa do Surge.

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Obtenha um perfil completo no formato indicado acima. Importe o arquivo local ou a URL do perfil remoto compatível com este cliente, atualize-o e selecione esse perfil. Não presuma que assinaturas comuns de nós e configurações de outros aplicativos sejam intercambiáveis.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Formato de importação:** URI / Base64 · Clash proxies · sing-box outbounds

A importação de assinaturas extrai os nós compatíveis; não presuma que as regras e outras configurações do perfil original sejam preservadas.

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Formato de importação:** Shadowrocket subscriptions / profiles

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Prepare uma assinatura de nós ou uma configuração de nó individual compatível com este aplicativo. Adicione-a pelo método de importação descrito na documentação do aplicativo, atualize as assinaturas quando houver suporte e confira se os nós aparecem. Uma lista de nós e um perfil completo de roteamento são entradas diferentes.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

- [Informações oficiais do produto [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Formato de importação:** Stash / Clash YAML

### Configuração rápida

1. Obtenha um perfil YAML completo compatível com Clash/Mihomo. Importe-o como perfil local ou remoto, atualize-o e selecione-o. A assinatura comum indicada acima não é um perfil YAML completo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Formato de importação:** URI / Base64 · Loon configuration

O Loon usa seus próprios formatos de configuração e de nós por assinatura. Verifique cada protocolo e campo em vez de presumir compatibilidade total com Surge ou Clash.

### Configuração rápida

1. Adicione uma URL de nó compatível ou uma assinatura comum URI/Base64 na área de assinaturas ou perfis do cliente. Atualize a assinatura e confirme que os nós esperados aparecem.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Formato de importação:** Egern Profile.yaml / proxies YAML

Egern YAML é um formato de perfil próprio, não Clash/Mihomo YAML.

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Obtenha um perfil completo no formato indicado acima. Importe o arquivo local ou a URL do perfil remoto compatível com este cliente, atualize-o e selecione esse perfil. Não presuma que assinaturas comuns de nós e configurações de outros aplicativos sejam intercambiáveis.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Formato de importação:** Supported node configurations

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Prepare uma assinatura de nós ou uma configuração de nó individual compatível com este aplicativo. Adicione-a pelo método de importação descrito na documentação do aplicativo, atualize as assinaturas quando houver suporte e confira se os nós aparecem. Uma lista de nós e um perfil completo de roteamento são entradas diferentes.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

- [Informações oficiais do produto [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Formato de importação:** Mihomo / Clash YAML · supported node links

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Obtenha um perfil YAML completo compatível com Clash/Mihomo. Importe-o como perfil local ou remoto, atualize-o e selecione-o. A assinatura comum indicada acima não é um perfil YAML completo.
2. Se o perfil oferecer essa opção, escolha um nó ou grupo de proxies e ative o modo proxy/VPN descrito na documentação do cliente. Conceda a permissão de VPN do sistema operacional somente ao aplicativo oficial que você instalou. Confirme o acesso real após conectar.
3. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

- [Informações oficiais do produto [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Formato de importação:** Clash / Mihomo YAML

### Configuração rápida

1. Antes da instalação, verifique o firmware, a arquitetura da CPU, os pacotes necessários e a memória disponível. Faça uma cópia de segurança da configuração do roteador e mantenha uma conexão de gerenciamento funcionando. Importe somente uma assinatura ou perfil compatível, atualize-o, escolha o nó ou grupo de saída e ative o plugin conforme as instruções oficiais.
2. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Formato de importação:** Supported node URI subscriptions

A importação de assinaturas extrai os nós compatíveis; não presuma que as regras e outras configurações do perfil original sejam preservadas.

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Antes da instalação, verifique o firmware, a arquitetura da CPU, os pacotes necessários e a memória disponível. Faça uma cópia de segurança da configuração do roteador e mantenha uma conexão de gerenciamento funcionando. Importe somente uma assinatura ou perfil compatível, atualize-o, escolha o nó ou grupo de saída e ative o plugin conforme as instruções oficiais.
2. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Referência técnica [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Formato de importação:** Mihomo YAML: proxies / proxy-providers

### Configuração rápida

1. Antes da instalação, verifique o firmware, a arquitetura da CPU, os pacotes necessários e a memória disponível. Faça uma cópia de segurança da configuração do roteador e mantenha uma conexão de gerenciamento funcionando. Importe somente uma assinatura ou perfil compatível, atualize-o, escolha o nó ou grupo de saída e ative o plugin conforme as instruções oficiais.
2. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

[Guia oficial [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Formato de importação:** HomeProxy node subscriptions

O HomeProxy gerencia nós e assinaturas pela própria interface. Verifique os formatos compatíveis com a versão instalada; usar sing-box internamente não significa que qualquer perfil sing-box JSON completo possa ser importado.

A orientação oficial para usuários é limitada; use as etapas resumidas de configuração e a referência oficial de formato verificada abaixo.

### Configuração rápida

1. Antes da instalação, verifique o firmware, a arquitetura da CPU, os pacotes necessários e a memória disponível. Faça uma cópia de segurança da configuração do roteador e mantenha uma conexão de gerenciamento funcionando. Importe somente uma assinatura ou perfil compatível, atualize-o, escolha o nó ou grupo de saída e ative o plugin conforme as instruções oficiais.
2. Se a atualização falhar, verifique a URL, a rede e o erro HTTP. Se a análise do conteúdo falhar, verifique o formato e a versão do núcleo. Se a importação funcionar, mas a conexão falhar, atualize, tente outro nó compatível e consulte o registro de erros do cliente. Uma atualização ou teste de latência bem-sucedido não garante disponibilidade nem segurança.

Verifique os protocolos compatíveis e a versão do núcleo instalada. A importação de nós não garante a transferência de todas as regras, configurações de DNS ou campos avançados.

Este guia resumido apresenta o formato de entrada verificado e o procedimento básico. As referências técnicas vinculadas não são um tutorial passo a passo para usuários; os nomes na interface podem variar conforme a versão.

- [Referência técnica [English]](https://github.com/immortalwrt/homeproxy)
