# Guides de configuration des clients

Choisissez d’abord le client, puis vérifiez son format d’entrée. Pour chaque langue, les liens GitHub et Cloudflare de ce projet fournissent le même abonnement ordinaire de nœuds URI/Base64 ; ce ne sont pas des profils complets Clash/Mihomo YAML ou sing-box JSON natifs.

Conservez les URL d’abonnement privées et les identifiants sur votre propre appareil. Ne les transmettez pas à des sites publics de conversion. Si un autre format est nécessaire, demandez un profil compatible à votre fournisseur ou préparez-le localement à l’aide de la documentation officielle de configuration du client cible.

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

**Format d’importation:** URI / Base64

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Format d’importation:** Clash / Mihomo YAML

### Configuration rapide

1. Procurez-vous un profil YAML complet compatible avec Clash/Mihomo. Importez-le comme profil local ou distant, actualisez-le et sélectionnez-le. L’abonnement ordinaire indiqué ci-dessus n’est pas un profil YAML complet.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Format d’importation:** URI / Base64 · Clash YAML · sing-box JSON

Ce client peut lire plusieurs formats, mais utilisez l’importation ordinaire URI/Base64 pour l’abonnement de ce projet. Les profils JSON et YAML natifs conservent leurs propres exigences.

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Format d’importation:** Clash / Mihomo YAML

### Configuration rapide

1. Procurez-vous un profil YAML complet compatible avec Clash/Mihomo. Importez-le comme profil local ou distant, actualisez-le et sélectionnez-le. L’abonnement ordinaire indiqué ci-dessus n’est pas un profil YAML complet.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Format d’importation:** Clash / Mihomo YAML

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Procurez-vous un profil YAML complet compatible avec Clash/Mihomo. Importez-le comme profil local ou distant, actualisez-le et sélectionnez-le. L’abonnement ordinaire indiqué ci-dessus n’est pas un profil YAML complet.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Format d’importation:** URI / Base64 · Clash YAML · sing-box JSON

Ce client peut lire plusieurs formats, mais utilisez l’importation ordinaire URI/Base64 pour l’abonnement de ce projet. Les profils JSON et YAML natifs conservent leurs propres exigences.

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Format d’importation:** URI / Base64 · sing-box JSON · Clash YAML proxies

L’importation d’un abonnement extrait les nœuds pris en charge ; ne présumez pas que les règles et les autres paramètres du profil d’origine sont conservés.

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Format d’importation:** Surge INI / Managed Profile

Utilisez une configuration Surge ou l’URL d’une configuration gérée. Ne considérez pas un abonnement V2Ray général comme une configuration Surge complète.

### Configuration rapide

1. Procurez-vous un profil complet au format indiqué ci-dessus. Importez le fichier local ou l’URL du profil distant pris en charge par ce client, actualisez-le, puis sélectionnez ce profil. Ne présumez pas que les abonnements ordinaires de nœuds et les configurations d’autres applications sont interchangeables.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Format d’importation:** Quantumult X / server_remote

Quantumult X utilise sa propre configuration et des ressources de serveurs distants ; une configuration complète et une ressource de nœuds sont des entrées différentes.

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Procurez-vous un profil complet au format indiqué ci-dessus. Importez le fichier local ou l’URL du profil distant pris en charge par ce client, actualisez-le, puis sélectionnez ce profil. Ne présumez pas que les abonnements ordinaires de nœuds et les configurations d’autres applications sont interchangeables.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Format d’importation:** sing-box JSON

### Configuration rapide

1. Procurez-vous un profil sing-box JSON complet adapté à la version du cœur du client. Ajoutez-le comme profil local ou distant, puis actualisez-le. Une liste d’URL de nœuds ou un fichier YAML de Clash ne peut pas servir de profil sing-box JSON natif.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Format d’importation:** URI / Base64

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Format d’importation:** Clash / Mihomo YAML

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Procurez-vous un profil YAML complet compatible avec Clash/Mihomo. Importez-le comme profil local ou distant, actualisez-le et sélectionnez-le. L’abonnement ordinaire indiqué ci-dessus n’est pas un profil YAML complet.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Référence technique [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Format d’importation:** Surfboard / Surge profile

Utilisez une configuration Surge ou l’URL d’une configuration gérée. Ne considérez pas un abonnement V2Ray général comme une configuration Surge complète.

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Procurez-vous un profil complet au format indiqué ci-dessus. Importez le fichier local ou l’URL du profil distant pris en charge par ce client, actualisez-le, puis sélectionnez ce profil. Ne présumez pas que les abonnements ordinaires de nœuds et les configurations d’autres applications sont interchangeables.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Format d’importation:** URI / Base64 · Clash proxies · sing-box outbounds

L’importation d’un abonnement extrait les nœuds pris en charge ; ne présumez pas que les règles et les autres paramètres du profil d’origine sont conservés.

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Format d’importation:** Shadowrocket subscriptions / profiles

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Préparez un abonnement de nœuds ou la configuration d’un nœud individuel pris en charge par cette application. Ajoutez-le avec la méthode d’importation décrite dans sa documentation, actualisez les abonnements si cette fonction est prise en charge et vérifiez que les nœuds apparaissent. Une liste de nœuds et un profil complet de routage sont des entrées différentes.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

- [Informations officielles sur le produit [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Format d’importation:** Stash / Clash YAML

### Configuration rapide

1. Procurez-vous un profil YAML complet compatible avec Clash/Mihomo. Importez-le comme profil local ou distant, actualisez-le et sélectionnez-le. L’abonnement ordinaire indiqué ci-dessus n’est pas un profil YAML complet.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Format d’importation:** URI / Base64 · Loon configuration

Loon utilise ses propres formats de configuration et de nœuds abonnés. Vérifiez chaque protocole et chaque champ au lieu de supposer une compatibilité totale avec Surge ou Clash.

### Configuration rapide

1. Ajoutez une URL de nœud prise en charge ou un abonnement ordinaire URI/Base64 dans la rubrique des abonnements ou des profils du client. Actualisez l’abonnement et vérifiez que les nœuds attendus apparaissent.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Format d’importation:** Egern Profile.yaml / proxies YAML

Egern YAML est un format de profil propre à Egern, et non Clash/Mihomo YAML.

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Procurez-vous un profil complet au format indiqué ci-dessus. Importez le fichier local ou l’URL du profil distant pris en charge par ce client, actualisez-le, puis sélectionnez ce profil. Ne présumez pas que les abonnements ordinaires de nœuds et les configurations d’autres applications sont interchangeables.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Format d’importation:** Supported node configurations

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Préparez un abonnement de nœuds ou la configuration d’un nœud individuel pris en charge par cette application. Ajoutez-le avec la méthode d’importation décrite dans sa documentation, actualisez les abonnements si cette fonction est prise en charge et vérifiez que les nœuds apparaissent. Une liste de nœuds et un profil complet de routage sont des entrées différentes.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

- [Informations officielles sur le produit [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Format d’importation:** Mihomo / Clash YAML · supported node links

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Procurez-vous un profil YAML complet compatible avec Clash/Mihomo. Importez-le comme profil local ou distant, actualisez-le et sélectionnez-le. L’abonnement ordinaire indiqué ci-dessus n’est pas un profil YAML complet.
2. Si le profil propose un choix, sélectionnez un nœud ou un groupe de proxys, puis activez le mode proxy/VPN décrit dans la documentation du client. Accordez l’autorisation VPN du système d’exploitation uniquement à l’application officielle que vous avez installée. Vérifiez l’accès réel après la connexion.
3. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

- [Informations officielles sur le produit [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Format d’importation:** Clash / Mihomo YAML

### Configuration rapide

1. Avant l’installation, vérifiez le micrologiciel, l’architecture du processeur, les paquets nécessaires et la mémoire disponible. Sauvegardez la configuration du routeur et conservez une connexion d’administration fonctionnelle. Importez uniquement un abonnement ou un profil pris en charge, actualisez-le, choisissez le nœud ou le groupe de sortie et activez le module selon ses instructions officielles.
2. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Format d’importation:** Supported node URI subscriptions

L’importation d’un abonnement extrait les nœuds pris en charge ; ne présumez pas que les règles et les autres paramètres du profil d’origine sont conservés.

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Avant l’installation, vérifiez le micrologiciel, l’architecture du processeur, les paquets nécessaires et la mémoire disponible. Sauvegardez la configuration du routeur et conservez une connexion d’administration fonctionnelle. Importez uniquement un abonnement ou un profil pris en charge, actualisez-le, choisissez le nœud ou le groupe de sortie et activez le module selon ses instructions officielles.
2. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Référence technique [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Format d’importation:** Mihomo YAML: proxies / proxy-providers

### Configuration rapide

1. Avant l’installation, vérifiez le micrologiciel, l’architecture du processeur, les paquets nécessaires et la mémoire disponible. Sauvegardez la configuration du routeur et conservez une connexion d’administration fonctionnelle. Importez uniquement un abonnement ou un profil pris en charge, actualisez-le, choisissez le nœud ou le groupe de sortie et activez le module selon ses instructions officielles.
2. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

[Guide officiel [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Format d’importation:** HomeProxy node subscriptions

HomeProxy gère les nœuds et les abonnements dans sa propre interface. Vérifiez les formats pris en charge par la version installée ; l’utilisation interne de sing-box ne signifie pas que tout profil sing-box JSON complet peut être importé.

Les guides officiels destinés aux utilisateurs sont limités ; suivez les étapes de configuration succinctes et la référence officielle de format vérifiée ci-dessous.

### Configuration rapide

1. Avant l’installation, vérifiez le micrologiciel, l’architecture du processeur, les paquets nécessaires et la mémoire disponible. Sauvegardez la configuration du routeur et conservez une connexion d’administration fonctionnelle. Importez uniquement un abonnement ou un profil pris en charge, actualisez-le, choisissez le nœud ou le groupe de sortie et activez le module selon ses instructions officielles.
2. Si l’actualisation échoue, vérifiez l’URL, le réseau et l’erreur HTTP. Si l’analyse échoue, vérifiez le format et la version du cœur. Si l’importation réussit mais que la connexion échoue, actualisez l’abonnement, essayez un autre nœud pris en charge, puis consultez le journal d’erreurs du client. Une actualisation ou un test de latence réussi ne garantit ni disponibilité ni sécurité.

Vérifiez les protocoles pris en charge et la version du cœur installée. L’importation des nœuds ne garantit pas le transfert de toutes les règles, des paramètres DNS ou des champs avancés.

Ce guide concis présente le format d’entrée vérifié et la procédure de base. Les références techniques indiquées ne constituent pas un tutoriel pas à pas pour les utilisateurs ; les libellés de l’interface peuvent varier selon la version.

- [Référence technique [English]](https://github.com/immortalwrt/homeproxy)
