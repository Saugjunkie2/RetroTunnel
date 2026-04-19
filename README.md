# RetroTunnel

![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)
![Status: M2 In Progress](https://img.shields.io/badge/Phase-M2%20In%20Progress-yellow.svg)
![Platform: Debian 13](https://img.shields.io/badge/Platform-Debian%2013-informational.svg)

Debian-basierter Dual-Tunnel VPN-Stack, der zwei grundverschiedene Client-Welten auf einem Server bedient:

- **L2TP_IPSEC** — Windows XP / Vista über L2TP/IPsec (accel-ppp)
- **WIREGUARD**  — Alle modernen Geräte über AmneziaWireGuard (DPI-resistent)

Full-Tunnel VPN mit deterministischer Server-Side Policy, SQL-first AAA, rollenbasiertem Enforcement, DNS-Zwang, internem Webpanel und einem produktionsfähigen Betriebsmodell.

## Warum existiert dieses Projekt?

RetroTunnel ist der Nachfolger von **xp-vpn-stack** (8 Monate Konzeptarbeit). Der Vorgänger nutzte IKEv2 (strongSwan) für den WIREGUARD-Pfad (damals als „MODERN" bezeichnet). IKEv2 wurde nach der ersten Implementierungsphase verworfen, weil:

1. **DNS-Zwang nicht durchsetzbar** — IKEv2/XFRM hat keine dedizierten Client-Interfaces, nftables konnte den Traffic nicht interface-basiert filtern. Das bricht das gesamte Sicherheitsmodell (8 AdGuard-Blocklisten wirkungslos).
2. **Client-Einrichtung zu komplex** — Windows 11 brauchte manuelle IPv6-Routen, Android brauchte die strongSwan-App.
3. **QoS unlösbar** — IKEv2 hat keine pppX-Interfaces, tc pro Client war nicht anwendbar.

AmneziaWireGuard löst alle drei Probleme: Dediziertes Interface (awg0), native Apps, tc-basiertes QoS pro Peer, und zusätzlich DPI-Obfuskation.

## Architektur auf einen Blick

### Dual-Tunnel

| Eigenschaft | L2TP_IPSEC | WIREGUARD |
|---|---|---|
| Protokoll | L2TP/IPsec | AmneziaWireGuard |
| Daemon | accel-ppp | awg (WireGuard-Fork) |
| Auth | RADIUS (MSCHAPv2) | PublicKey |
| IPv6 | Nein | Ja (Dualstack) |
| Interface | pppX (pro Client) | awg0 (shared) |
| QoS | tc auf pppX | tc auf awg0 per Peer |
| Session-Erkennung | RADIUS Accounting | Polling (last_handshake) |

### Vier Rollen

| Rolle | Speed/BW | Connections | Restricted-fähig | Panel-Zugriff |
|---|---|---|---|---|
| USER | Per Plan | Per Plan | Ja | User-Panel |
| VIP | Kein Limit | 3 (Default, individualisierbar) | Ja | User-Panel |
| MODERATOR | Kein Limit | 3 (Default, individualisierbar) | Ja | User-Panel + teilw. Admin |
| ADMIN | Kein Limit | Unbegrenzt | Nein (Not-Aus = DISABLE) | Vollzugriff |

Rollen gehören zum **Customer** (Webpanel-Rang), nicht zur Connection. Alle Connections eines Customers erben dieselbe Rolle. Connection-Limits leben im Policy-System ([D003](decisions/D003_POLICY_SYSTEM_UND_ROLLE_AM_CUSTOMER.txt)).

### IP-Pools (pro Rolle, unabhängig vom Tunnel-Typ)

| Pool | IPv4 CIDR | IPv6 CIDR | Kapazität |
|---|---|---|---|
| SERVICE_NET | 10.77.0.0/28 | fd77:0:0:0::/64 | 7 Anchors |
| ADMIN | 10.77.2.0/24 | fd77:0:0:2::/64 | 253 Slots |
| MODERATOR | 10.77.3.0/24 | fd77:0:0:3::/64 | 253 Slots |
| VIP | 10.77.4.0/22 | fd77:0:0:4::/62 | 1021 Slots |
| USER | 10.77.16.0/20 | fd77:0:0:10::/60 | 4093 Slots |

Ein Admin mit einem XP-Gerät (L2TP_IPSEC) und einem Android (WIREGUARD) bekommt beide IPs aus dem ADMIN-Pool. `tunnel_type` bestimmt nur den technischen Pfad, nicht die Rechte.

## Design-Prinzipien

| # | Prinzip | Kurzform |
|---|---|---|
| DP-01 | VPN ist nur der Tunnel | Policies leben in Linux (nftables, tc, SQL) |
| DP-02 | SQL-first | Keine Magic Numbers, zwei getrennte Domänen (Settings + Policy) |
| DP-03 | DNS-Zwang ist nicht verhandelbar | DNAT53 für alle, DoT/DoQ geblockt |
| DP-04 | Fail-Closed | Kein Client bekommt WAN vor Policy-Apply |
| DP-05 | Deterministische Enforcement | FLUSH+REBUILD Reconcile, Hard-Cut |
| DP-06 | Rollen über IP-Ranges | CIDR-Match in nftables, O(1), kein Sync |
| DP-07 | Webpanel ist die Zentrale | Nur im VPN erreichbar, Single Surface |
| DP-08 | Plans über Leistung, nicht Sicherheit | QoS/Quota ja, DNS-Zwang nein |

Vollständige Beschreibung: [`00_MANIFEST.txt`](00_MANIFEST.txt) §3.

## Projektstruktur

> **Reifehinweis:** Die folgende Baumstruktur zeigt die **Ziel-Architektur**. Nur mit ✅ markierte Ordner haben normativen Inhalt. Ordner ohne Markierung sind Platzhalter für zukünftige Arbeitspakete (M2-M4). `model/` enthält das durchreviewte Denkmodell (DEPRECATED — wird bei Base-Ausarbeitung aufgelöst). Der aktuelle Arbeitsstand ist in der Status-Tabelle am Ende dokumentiert.

```
RetroTunnel/
├── 00_MANIFEST.txt                 Grundentscheidungen, Design-Prinzipien
├── 01_GLOSSARY.txt                 Kanonische Begriffe + PREFIX-LEGENDE
├── 02_ASSUMPTIONS_AND_RULES.txt    17 System-Regeln, 9 Annahmen
├── 03_CHANGELOG.txt                Zentrale Projekthistorie
├── README.md                       Dieses Dokument
├── LICENSE                         MIT
│
│   # Governance / Steuerung (Claude AI Co-Architect)
├── CLAUDE_BRIEFING.txt             Handoff für neue Claude-Instanzen
├── REVIEW_STANDARD.txt             Review-Methodik, 8 Prüfebenen
├── REVIEW_TRACKER.txt              Datei-Inventar, Review-Status
├── PRIORITAETENLISTE.txt           Arbeitspakete (M0–M4)
├── NAVIGATIONSKARTE_ALTES_KONZEPT.txt  Themen-Index Vorgänger
│
├── model/                          DAS DENKMODELL (Was + Warum)
│   │                               (wird schrittweise in zuständige Bases aufgelöst)
│   ├── DOMAIN_MODEL.txt            Entitäten, Beziehungen, Invarianten → BASE-010
│   ├── TRUTH_MODEL.txt             Source-of-Truth Map → BASE-000 + BASE-090
│   ├── NETWORK_MODEL.txt           Pools, Segmente → BASE-010 + BASE-005
│   └── state_machines/
│       ├── SM_CONNECTION.txt       Connection-Lifecycle → BASE-010
│       ├── SM_SESSION.txt          Session-Lifecycle → BASE-070
│       ├── SM_ONBOARDING.txt       Verify-Wall, Claim → MOD-001
│       └── SM_POLICY_RESTRICT.txt  Enforcement → BASE-080
│
├── base/                           KERN-MODULE (Minimum Viable System)
│   ├── BASE-000_SQL_FIRST/         SQL-first Governance, Naming, Registry ✅
│   ├── BASE-005_PLATFORM_CORE/     OS-Baseline, Endpoints, Lifecycle ✅
│   ├── BASE-010_IDENTITY_CORE/     Customers, Connections, Rollen ✅
│   ├── BASE-020_AAA_CORE/          FreeRADIUS + SQL-first ✅
│   ├── BASE-030_TUNNEL_L2TP_IPSEC/ L2TP/IPsec (accel-ppp + strongSwan) ✅
│   ├── BASE-040_TUNNEL_WIREGUARD/  AmneziaWireGuard
│   ├── BASE-050_FIREWALL_CORE/     nftables, NAT, Peer-Isolation
│   ├── BASE-060_DNS_CORE/          Unbound + AdGuard + DNAT53
│   ├── BASE-070_SESSION_CORE/      Mapping, Locks, Janitor
│   ├── BASE-080_POLICY_APPLY_CORE/ Apply, Reconcile, Hard-Cut
│   ├── BASE-090_SETTINGS_CORE/     SQL-first Settings-System
│   ├── BASE-100_POLICY_CORE/       Policy-System (D003)
│   └── BASE-110_WEBSTACK_CORE/     OpenResty + PHP-FPM + DB
│
├── modules/                        ERWEITERUNGEN (Features)
│   ├── MOD-001_ONBOARDING/         Verify-Wall, Claim, Grace
│   ├── MOD-002_RESTRICTED_MODE/    Walled Garden, Hard-Cut
│   ├── MOD-003_QOS/                tc/CAKE, Speed-Limiting
│   ├── MOD-004_BLOCKPAGE_CA/       MITM, interne CA
│   ├── MOD-005_FAIL2BAN/           Event-Klassifikation
│   ├── MOD-006_PANEL_FEATURES/     User/Admin Views
│   ├── MOD-007_LOGGING_MONITORING/ Retention, Alerts
│   ├── MOD-008_BACKUP_DR/          Backup/Restore
│   ├── MOD-009_PEAK_MODE/          CPU-Overload Schutz
│   └── MOD-010_PLANS/              Tarife, Quota, Billing
│
├── decisions/                      Architecture Decision Records
├── proofs/                         Tests, Acceptance, DoD
├── implementation/                 Configs, Guides, Build-Order
├── docs/                           Referenz-Dokumente
└── entwuerfe/                      Ideen, Diskussionen (NICHT normativ)
```

Das Schichtenmodell folgt der Regel: `model/` (Denkmodell) → `base/` (Kern) → `modules/` (Features). Ein Modul darf Base referenzieren, aber Base darf nie ein Modul voraussetzen (KR-02).

Seit 2026-04-16 ist die Nummerierung konsequent 3-stellig: Base-Ordner BASE-000 bis BASE-110, Module MOD-001 bis MOD-010, Dateinummern innerhalb Ordnern 000..095. Roter Faden durchs Konzept, Einfügepuffer für spätere Erweiterungen.

## Dokumentation — Einstiegspunkte

| Datei | Inhalt |
|---|---|
| `00_MANIFEST.txt` | Design-Prinzipien, Architektur-Achsen, Ordnerstruktur, Vorgänger-Referenz |
| `01_GLOSSARY.txt` | Kanonische Begriffe + PREFIX-LEGENDE (alle Identifier-Namensräume) |
| `02_ASSUMPTIONS_AND_RULES.txt` | 17 bindende System-Regeln, 9 Annahmen, 5 Nicht-Annahmen |
| `base/BASE-000_SQL_FIRST/` | SQL-first Governance: Prefixe, Naming, Registry, Auth-Split |
| `base/BASE-005_PLATFORM_CORE/` | Plattform-Grundnorm: OS, Endpoints, Users, Secrets, Lifecycle |
| `model/DOMAIN_MODEL.txt` | Zwei-Ebenen-Modell, Policy-System, reason_registry, Zählregel |
| `model/TRUTH_MODEL.txt` | Source-of-Truth Map — welche Tabelle/welches Set ist SoT für was |
| `model/NETWORK_MODEL.txt` | IP-Pools, Service-Anchors, Slot-Mapping, Pool-Regeln |
| `decisions/D002_*.txt` | Rollenwechsel: In-Place Mutation statt DISABLE+INSERT |
| `decisions/D003_*.txt` | Policy-System: Getrennt von Settings, Rolle am Customer |

Governance-Dateien für die Zusammenarbeit mit Claude (AI Co-Architect):

| Datei | Inhalt |
|---|---|
| `CLAUDE_BRIEFING.txt` | Handoff-Dokument für neue Claude-Instanzen |
| `REVIEW_STANDARD.txt` | Review-Methodik, 8 Prüfebenen, Autonomie-Grenze |
| `REVIEW_TRACKER.txt` | Datei-Inventar, Review-Status, Sweep-Plan, Exit-Kriterien |
| `PRIORITAETENLISTE.txt` | Arbeitspakete in 5 Modellphasen (M0–M4) |
| `NAVIGATIONSKARTE_ALTES_KONZEPT.txt` | Themen-Index zum Vorgänger xp-vpn-stack |

## Voraussetzungen

| Komponente | Version / Anforderung |
|---|---|
| OS | Debian 13 (Trixie) |
| Datenbank | MariaDB 11.8+ |
| VPN (L2TP_IPSEC) | accel-ppp (L2TP/IPsec) |
| VPN (WIREGUARD) | AmneziaWireGuard |
| DNS | Unbound + AdGuardHome |
| Webserver | OpenResty + PHP-FPM |
| Firewall | nftables |
| Netzwerk | 1 Gbit/s, 40 TB/Monat, Single Server |
| E-Mail | Funktionaler E-Mail-Server (SPF/DKIM/DMARC) |

## Server

| Parameter | Wert |
|---|---|
| Standort | Schweiz |
| FQDN | rt-gw-001.v6.rocks |
| IPv4 | 185.150.28.184 |
| IPv6 | 2a07:6d80:1e01:145d::1 |
| OS | Debian 13 (Trixie) |
| DB | MariaDB 11.8.6 |
| WAN-Interface | ens18 |
| Bandbreite | 1 Gbit/s |
| Volume | 40 TB/Monat (danach 100 Mbit/s) |

## Status

| Phase | Inhalt | Status |
|---|---|---|
| M0 | Fundament (Manifest, Rules, Glossar) | ✅ Done |
| M1 | Denkmodell (7 Model-Dateien, 2 Decisions) | ✅ Done |
| M2-000 | BASE-000_SQL_FIRST (Governance, Naming, Registry) | ✅ Done |
| M2-005 | BASE-005_PLATFORM_CORE (Grundnorm OS/Lifecycle) | ✅ Done |
| M2-010 | BASE-010_IDENTITY_CORE (Schema, Lifecycle, Write-Path) | ✅ Done |
| M2-020 | BASE-020_AAA_CORE (Admission, RADIUS, WG-Vertrag) | ✅ Done |
| M2-030 | BASE-030_TUNNEL_L2TP_IPSEC (accel-ppp + strongSwan) | ✅ Done |
| M2-040..110 | Rest der Kern-Module (8 Base-Module) | ⬜ Waiting |
| M3 | Erweiterungs-Module (10 Module) | ⏸ Deferred |
| M4 | Decisions, Proofs, Implementation | ⏸ Deferred |

## Vorgänger

Das vollständige Vorgänger-Konzept (xp-vpn-stack, 8 Monate, 57 Blocks, 12 Decisions) liegt unter `../xp-vpn-stack/`. Architekturentscheidungen werden nicht blind übernommen — sie müssen im neuen Konzept explizit bestätigt oder geändert werden. Details zu Übernahmen und Änderungen: [`00_MANIFEST.txt`](00_MANIFEST.txt) §5.

**Begriffs-Brücke Alt ↔ Neu:** Im Altkonzept hießen die beiden Tunnel-Welten LEGACY (L2TP/IPsec für XP) und MODERN (damals IKEv2, heute WireGuard). In RetroTunnel sind die kanonischen Begriffe L2TP_IPSEC und WIREGUARD. Die NAVIGATIONSKARTE erklärt die Begriffs-Brücke im Detail.

## Contributing

Dieses Projekt wird von Marco (Owner) und Claude (AI Co-Architect) bearbeitet. Externe Beiträge sind aktuell nicht vorgesehen. Das Konzept dient als Grundlage für eine produktive Single-Server VPN-Infrastruktur.

## Lizenz

MIT — siehe [LICENSE](LICENSE).
