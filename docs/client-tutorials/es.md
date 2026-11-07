# Guías de configuración de clientes

Elija primero el cliente y compruebe el formato que admite. Los enlaces de GitHub y Cloudflare de este proyecto proporcionan, para cada idioma, la misma suscripción ordinaria de nodos URI/Base64; no son perfiles completos de Clash/Mihomo YAML ni de sing-box JSON nativo.

Mantenga las URL de suscripción privadas y las credenciales en su propio dispositivo. No las envíe a sitios públicos de conversión. Si necesita otro formato, obtenga un perfil compatible de su proveedor o prepárelo localmente siguiendo la documentación oficial de configuración del cliente de destino.

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

**Formato de importación:** URI / Base64

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Formato de importación:** Clash / Mihomo YAML

### Configuración rápida

1. Obtenga un perfil YAML completo compatible con Clash/Mihomo. Impórtelo como perfil local o remoto, actualícelo y selecciónelo. La suscripción ordinaria indicada arriba no es un perfil YAML completo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Formato de importación:** URI / Base64 · Clash YAML · sing-box JSON

Este cliente puede leer varios formatos, pero para la suscripción de este proyecto debe utilizar la importación ordinaria URI/Base64. Los perfiles JSON y YAML nativos siguen teniendo sus propios requisitos.

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Formato de importación:** Clash / Mihomo YAML

### Configuración rápida

1. Obtenga un perfil YAML completo compatible con Clash/Mihomo. Impórtelo como perfil local o remoto, actualícelo y selecciónelo. La suscripción ordinaria indicada arriba no es un perfil YAML completo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Formato de importación:** Clash / Mihomo YAML

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Obtenga un perfil YAML completo compatible con Clash/Mihomo. Impórtelo como perfil local o remoto, actualícelo y selecciónelo. La suscripción ordinaria indicada arriba no es un perfil YAML completo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Formato de importación:** URI / Base64 · Clash YAML · sing-box JSON

Este cliente puede leer varios formatos, pero para la suscripción de este proyecto debe utilizar la importación ordinaria URI/Base64. Los perfiles JSON y YAML nativos siguen teniendo sus propios requisitos.

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Formato de importación:** URI / Base64 · sing-box JSON · Clash YAML proxies

La importación de suscripciones extrae los nodos compatibles; no presuponga que se conservan las reglas y otros ajustes del perfil original.

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Formato de importación:** Surge INI / Managed Profile

Utilice una configuración de Surge o una URL de configuración administrada. No trate una suscripción V2Ray general como una configuración completa de Surge.

### Configuración rápida

1. Obtenga un perfil completo en el formato indicado arriba. Importe el archivo local o la URL de perfil remoto que admita este cliente, actualícelo y seleccione ese perfil. No dé por hecho que las suscripciones ordinarias de nodos y las configuraciones de otras aplicaciones son intercambiables.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Formato de importación:** Quantumult X / server_remote

Quantumult X utiliza su propia configuración y recursos de servidores remotos; una configuración completa y un recurso de nodos son entradas diferentes.

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Obtenga un perfil completo en el formato indicado arriba. Importe el archivo local o la URL de perfil remoto que admita este cliente, actualícelo y seleccione ese perfil. No dé por hecho que las suscripciones ordinarias de nodos y las configuraciones de otras aplicaciones son intercambiables.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Formato de importación:** sing-box JSON

### Configuración rápida

1. Obtenga un perfil sing-box JSON completo que corresponda a la versión del núcleo del cliente. Añádalo como perfil local o remoto y actualícelo. Una lista de URL de nodos o un archivo YAML de Clash no se puede utilizar como sing-box JSON nativo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Formato de importación:** URI / Base64

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Formato de importación:** Clash / Mihomo YAML

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Obtenga un perfil YAML completo compatible con Clash/Mihomo. Impórtelo como perfil local o remoto, actualícelo y selecciónelo. La suscripción ordinaria indicada arriba no es un perfil YAML completo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Referencia técnica [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Formato de importación:** Surfboard / Surge profile

Utilice una configuración de Surge o una URL de configuración administrada. No trate una suscripción V2Ray general como una configuración completa de Surge.

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Obtenga un perfil completo en el formato indicado arriba. Importe el archivo local o la URL de perfil remoto que admita este cliente, actualícelo y seleccione ese perfil. No dé por hecho que las suscripciones ordinarias de nodos y las configuraciones de otras aplicaciones son intercambiables.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Formato de importación:** URI / Base64 · Clash proxies · sing-box outbounds

La importación de suscripciones extrae los nodos compatibles; no presuponga que se conservan las reglas y otros ajustes del perfil original.

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Formato de importación:** Shadowrocket subscriptions / profiles

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Prepare una suscripción de nodos o una configuración de nodo individual compatible con esta aplicación. Añádala mediante el método de importación documentado, actualice las suscripciones cuando se admita y compruebe que aparecen los nodos. Una lista de nodos y un perfil completo de enrutamiento son entradas diferentes.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

- [Información oficial del producto [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Formato de importación:** Stash / Clash YAML

### Configuración rápida

1. Obtenga un perfil YAML completo compatible con Clash/Mihomo. Impórtelo como perfil local o remoto, actualícelo y selecciónelo. La suscripción ordinaria indicada arriba no es un perfil YAML completo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Formato de importación:** URI / Base64 · Loon configuration

Loon utiliza sus propios formatos de configuración y de nodos suscritos. Verifique cada protocolo y campo en lugar de suponer una compatibilidad total con Surge o Clash.

### Configuración rápida

1. Añada una URL de nodo compatible o una suscripción ordinaria URI/Base64 en la sección de suscripciones o perfiles del cliente. Actualice la suscripción y compruebe que aparecen los nodos esperados.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Formato de importación:** Egern Profile.yaml / proxies YAML

Egern YAML es un formato de perfil propio, no Clash/Mihomo YAML.

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Obtenga un perfil completo en el formato indicado arriba. Importe el archivo local o la URL de perfil remoto que admita este cliente, actualícelo y seleccione ese perfil. No dé por hecho que las suscripciones ordinarias de nodos y las configuraciones de otras aplicaciones son intercambiables.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Formato de importación:** Supported node configurations

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Prepare una suscripción de nodos o una configuración de nodo individual compatible con esta aplicación. Añádala mediante el método de importación documentado, actualice las suscripciones cuando se admita y compruebe que aparecen los nodos. Una lista de nodos y un perfil completo de enrutamiento son entradas diferentes.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

- [Información oficial del producto [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Formato de importación:** Mihomo / Clash YAML · supported node links

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Obtenga un perfil YAML completo compatible con Clash/Mihomo. Impórtelo como perfil local o remoto, actualícelo y selecciónelo. La suscripción ordinaria indicada arriba no es un perfil YAML completo.
2. Si el perfil permite elegir, seleccione un nodo o grupo de proxies y active el modo proxy/VPN descrito en la documentación del cliente. Conceda el permiso VPN del sistema operativo únicamente a la aplicación oficial que haya instalado. Compruebe el acceso real después de conectarse.
3. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

- [Información oficial del producto [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Formato de importación:** Clash / Mihomo YAML

### Configuración rápida

1. Antes de instalar, compruebe el firmware, la arquitectura de la CPU, los paquetes necesarios y la memoria disponible. Haga una copia de seguridad de la configuración del router y mantenga una conexión de administración operativa. Importe solo una suscripción o perfil compatible, actualícelo, elija el nodo o grupo de salida y active el complemento según sus instrucciones oficiales.
2. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Formato de importación:** Supported node URI subscriptions

La importación de suscripciones extrae los nodos compatibles; no presuponga que se conservan las reglas y otros ajustes del perfil original.

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Antes de instalar, compruebe el firmware, la arquitectura de la CPU, los paquetes necesarios y la memoria disponible. Haga una copia de seguridad de la configuración del router y mantenga una conexión de administración operativa. Importe solo una suscripción o perfil compatible, actualícelo, elija el nodo o grupo de salida y active el complemento según sus instrucciones oficiales.
2. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Referencia técnica [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Formato de importación:** Mihomo YAML: proxies / proxy-providers

### Configuración rápida

1. Antes de instalar, compruebe el firmware, la arquitectura de la CPU, los paquetes necesarios y la memoria disponible. Haga una copia de seguridad de la configuración del router y mantenga una conexión de administración operativa. Importe solo una suscripción o perfil compatible, actualícelo, elija el nodo o grupo de salida y active el complemento según sus instrucciones oficiales.
2. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

[Guía oficial [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Formato de importación:** HomeProxy node subscriptions

HomeProxy administra nodos y suscripciones mediante su propia interfaz. Compruebe los formatos que admite la versión instalada; utilizar sing-box internamente no significa que se pueda importar cualquier perfil sing-box JSON completo.

La orientación oficial para usuarios es limitada; siga los pasos breves de configuración y la referencia oficial de formato verificada que figura a continuación.

### Configuración rápida

1. Antes de instalar, compruebe el firmware, la arquitectura de la CPU, los paquetes necesarios y la memoria disponible. Haga una copia de seguridad de la configuración del router y mantenga una conexión de administración operativa. Importe solo una suscripción o perfil compatible, actualícelo, elija el nodo o grupo de salida y active el complemento según sus instrucciones oficiales.
2. Si falla la actualización, compruebe la URL, la red y el error HTTP. Si falla el análisis, compruebe el formato y la versión del núcleo. Si la importación funciona pero la conexión falla, actualice, pruebe otro nodo compatible y consulte el registro de errores del cliente. Una actualización o prueba de latencia correcta no garantiza disponibilidad ni seguridad.

Compruebe los protocolos admitidos y la versión del núcleo instalada. Importar nodos no garantiza la transferencia de todas las reglas, los ajustes DNS o los campos avanzados.

Esta guía breve explica el formato de entrada verificado y el procedimiento básico. Las referencias técnicas enlazadas no son un tutorial paso a paso para usuarios; los nombres de la interfaz pueden variar según la versión.

- [Referencia técnica [English]](https://github.com/immortalwrt/homeproxy)
