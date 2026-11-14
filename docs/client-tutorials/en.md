# Client configuration guides

Choose the client first, then check its input format. The GitHub and Cloudflare links in this project carry the same ordinary URI/Base64 node subscription for each language; they are not ready-made Clash/Mihomo YAML or native sing-box JSON profiles.

Keep private subscription URLs and credentials on your own device. Do not submit them to public conversion websites. If a different format is needed, obtain a compatible profile from your provider or prepare it locally using the target client's official configuration documentation.

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

**Import format:** URI / Base64

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [中文]](https://github.com/2dust/v2rayN/wiki/Description-of-some-ui)


<a id="clash-verge-rev"></a>

## Clash Verge Rev

**Import format:** Clash / Mihomo YAML

### Quick setup

1. Obtain a complete Clash/Mihomo-compatible YAML profile. Import it as a local or remote profile, update it and select it. The ordinary subscription above is not a complete YAML profile.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [中文]](https://www.clashverge.dev/guide/quickstart.html)


<a id="hiddify"></a>

## Hiddify

**Import format:** URI / Base64 · Clash YAML · sing-box JSON

This client can read several formats, but use the ordinary URI/Base64 import route for this project's subscription. Native JSON and YAML profiles still have their own requirements.

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://hiddify.com/app/How-to-use-Hiddify-app/)


<a id="clash-party"></a>

## Clash Party

**Import format:** Clash / Mihomo YAML

### Quick setup

1. Obtain a complete Clash/Mihomo-compatible YAML profile. Import it as a local or remote profile, update it and select it. The ordinary subscription above is not a complete YAML profile.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [中文]](https://clashparty.org/docs/handson)


<a id="flclash"></a>

## FlClash

**Import format:** Clash / Mihomo YAML

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Obtain a complete Clash/Mihomo-compatible YAML profile. Import it as a local or remote profile, update it and select it. The ordinary subscription above is not a complete YAML profile.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://github.com/chen08209/FlClash#usage)

<a id="karing"></a>

## Karing

**Import format:** URI / Base64 · Clash YAML · sing-box JSON

This client can read several formats, but use the ordinary URI/Base64 import route for this project's subscription. Native JSON and YAML profiles still have their own requirements.

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://karing.app/en/quickstart)


<a id="throne"></a>

## Throne

**Import format:** URI / Base64 · sing-box JSON · Clash YAML proxies

Subscription import extracts supported nodes; do not assume that rules and other settings from the original profile are preserved.

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://throneproj.github.io/get_started/configuration/)


<a id="surge"></a>

## Surge Mac

**Import format:** Surge INI / Managed Profile

Use a Surge configuration or managed configuration URL. Do not treat a general V2Ray subscription as a complete Surge configuration.

### Quick setup

1. Obtain a complete profile in the format shown above. Import the local file or remote profile URL supported by this client, update it, and select that profile. Do not assume that ordinary node subscriptions or another app's configuration are interchangeable.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://manual.nssurge.com/getting-started/quick-start.html)


<a id="quantumult-x"></a>

## Quantumult X

**Import format:** Quantumult X / server_remote

Quantumult X uses its own configuration and remote server resources; a full configuration and a node resource are different inputs.

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Obtain a complete profile in the format shown above. Import the local file or remote profile URL supported by this client, update it, and select that profile. Do not assume that ordinary node subscriptions or another app's configuration are interchangeable.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [中文 / English]](https://github.com/crossutility/Quantumult-X/blob/master/sample.conf)

<a id="sing-box"></a>

## sing-box for Apple platforms

**Import format:** sing-box JSON

### Quick setup

1. Obtain a complete sing-box JSON profile matching the client's core version. Add it as a local or remote profile and update it. A list of node URLs or a Clash YAML file cannot be used as native sing-box JSON.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://sing-box.sagernet.org/clients/general/)


<a id="v2rayng"></a>

## v2rayNG

**Import format:** URI / Base64

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://github.com/2dust/v2rayNG/wiki/Mode)

<a id="clash-meta-android"></a>

## Clash Meta for Android

**Import format:** Clash / Mihomo YAML

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Obtain a complete Clash/Mihomo-compatible YAML profile. Import it as a local or remote profile, update it and select it. The ordinary subscription above is not a complete YAML profile.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://wiki.metacubex.one/en/handbook/syntax/)
- [Technical reference [English]](https://github.com/MetaCubeX/ClashMetaForAndroid#automation)

<a id="surfboard"></a>

## Surfboard

**Import format:** Surfboard / Surge profile

Use a Surge configuration or managed configuration URL. Do not treat a general V2Ray subscription as a complete Surge configuration.

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Obtain a complete profile in the format shown above. Import the local file or remote profile URL supported by this client, update it, and select that profile. Do not assume that ordinary node subscriptions or another app's configuration are interchangeable.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://getsurfboard.com/docs/profile-format/overview/)

<a id="nekobox-android"></a>

## NekoBox for Android

**Import format:** URI / Base64 · Clash proxies · sing-box outbounds

Subscription import extracts supported nodes; do not assume that rules and other settings from the original profile are preserved.

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [中文]](https://matsuridayo.github.io/nb4a-configuration/)


<a id="shadowrocket"></a>

## Shadowrocket

**Import format:** Shadowrocket subscriptions / profiles

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Prepare a node subscription or individual node configuration supported by this app. Add it using the app’s documented import method, update subscriptions where supported, and check that nodes appear. A node list and a complete routing profile are different inputs.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

- [Official product information [English]](https://apps.apple.com/us/app/shadowrocket/id932747118)

<a id="stash"></a>

## Stash

**Import format:** Stash / Clash YAML

### Quick setup

1. Obtain a complete Clash/Mihomo-compatible YAML profile. Import it as a local or remote profile, update it and select it. The ordinary subscription above is not a complete YAML profile.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://stash.wiki/en/get-started)


<a id="loon"></a>

## Loon

**Import format:** URI / Base64 · Loon configuration

Loon uses its own configuration and subscribed node formats. Verify each protocol and field rather than assuming full compatibility with Surge or Clash.

### Quick setup

1. Add a supported node URL or ordinary URI/Base64 subscription in the client's subscription/profile area. Refresh the subscription and confirm that the expected nodes appear.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [English]](https://nsloon.app/en/docs/Node/subscription/)


<a id="egern"></a>

## Egern

**Import format:** Egern Profile.yaml / proxies YAML

Egern YAML is its own profile format, not Clash/Mihomo YAML.

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Obtain a complete profile in the format shown above. Import the local file or remote profile URL supported by this client, update it, and select that profile. Do not assume that ordinary node subscriptions or another app's configuration are interchangeable.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://egernapp.com/docs/configuration/policy_groups/)

<a id="streisand"></a>

## Streisand

**Import format:** Supported node configurations

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Prepare a node subscription or individual node configuration supported by this app. Add it using the app’s documented import method, update subscriptions where supported, and check that nodes appear. A node list and a complete routing profile are different inputs.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

- [Official product information [English]](https://streisand.pages.dev/)

<a id="potatso"></a>

## Potatso

**Import format:** Mihomo / Clash YAML · supported node links

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Obtain a complete Clash/Mihomo-compatible YAML profile. Import it as a local or remote profile, update it and select it. The ordinary subscription above is not a complete YAML profile.
2. Where the profile offers a choice, select a node or proxy group, then enable the client’s documented proxy/VPN mode. Grant the operating-system VPN permission only to the official app you installed. Confirm actual access after connecting.
3. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

- [Official product information [English]](https://potatso.com/)

<a id="openclash"></a>

## OpenClash

**Import format:** Clash / Mihomo YAML

### Quick setup

1. Before installation, check the firmware, CPU architecture, required packages and available memory. Back up the router configuration and keep a working management connection. Import only a supported subscription/profile, update it, choose the outbound node or group, and enable the plugin according to its official instructions.
2. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [中文]](https://github.com/vernesong/OpenClash#快速开始)


<a id="passwall"></a>

## PassWall2 / PassWall

**Import format:** Supported node URI subscriptions

Subscription import extracts supported nodes; do not assume that rules and other settings from the original profile are preserved.

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Before installation, check the firmware, CPU architecture, required packages and available memory. Back up the router configuration and keep a working management connection. Import only a supported subscription/profile, update it, choose the outbound node or group, and enable the plugin according to its official instructions.
2. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://github.com/Openwrt-Passwall/openwrt-passwall2)
- [Technical reference [English]](https://github.com/Openwrt-Passwall/openwrt-passwall)

<a id="nikki"></a>

## Nikki

**Import format:** Mihomo YAML: proxies / proxy-providers

### Quick setup

1. Before installation, check the firmware, CPU architecture, required packages and available memory. Back up the router configuration and keep a working management connection. Import only a supported subscription/profile, update it, choose the outbound node or group, and enable the plugin according to its official instructions.
2. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

[Official guide [中文]](https://github.com/nikkinikki-org/OpenWrt-nikki/wiki)


<a id="homeproxy"></a>

## HomeProxy

**Import format:** HomeProxy node subscriptions

HomeProxy manages nodes and subscriptions through its own interface. Check the formats supported by the installed version; using sing-box internally does not mean arbitrary full sing-box JSON profiles can be imported.

Official user guidance is limited; use the concise setup steps and the verified official format reference below.

### Quick setup

1. Before installation, check the firmware, CPU architecture, required packages and available memory. Back up the router configuration and keep a working management connection. Import only a supported subscription/profile, update it, choose the outbound node or group, and enable the plugin according to its official instructions.
2. If updating fails, check the URL, network and HTTP error. If parsing fails, check the format and core version. If importing succeeds but connecting fails, refresh and try another supported node, then inspect the client's error log. A successful update or latency test does not guarantee availability or safety.

Check the supported protocols and the installed core version; importing nodes does not guarantee that all rules, DNS settings or advanced fields will transfer.

This concise guide covers the verified input format and basic workflow. The linked technical references are not a step-by-step user tutorial; interface labels can vary by version.

- [Technical reference [English]](https://github.com/immortalwrt/homeproxy)
