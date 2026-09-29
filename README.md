# Testy engeto.cz (Playwright + pytest)

Automatizované end-to-end testy webové stránky https://engeto.cz, které
simulují reálné chování uživatele - klikání v menu, procházení podstránek
a přechod na externí web (jobs.cz).

## Co testy ověřují

- **test_volne_pozice_sporitelna** - cesta O nás → Zaměstnavatelé → detail
  firmy Česká spořitelna → zobrazení volných pozic na jobs.cz.
  Test ověřuje především funkčnost přechodu na externí web.
  
- **test_precteni_pribehu_absolventa** - cesta Kurzy → Testing Akademie →
  Příběhy a reference → otevření příběhu konkrétního absolventa.
  Test ověřuje funkčnost jak hlavního menu, tak postranního menu v sekci Testing akademie 
  a proklik na konktrétní příběh absolventa.
  
- **test_precteni_webinare_jak_se_stat_testerem** - cesta Průvodce IT → Blog
  → filtr Testing → otevření konkrétního článku.
  Test ověřuje funkčnost filtrování na stránce Blog a otevření konkrétního článku pod daným filtrem.

Všechny testy zároveň ověřují, že se korektně odbaví okno s cookies (jak na
engeto.cz, tak na jobs.cz).

## Požadavky

- Python 3.10+

## Instalace

pip install -r requirements.txt
playwright install


Druhý příkaz stáhne prohlížeče (Chromium, Firefox, WebKit), které Playwright
potřebuje ke spuštění testů.

## Spuštění testů
```bash
pytest
```

Testy běží defaultně v headless módu (bez zobrazení prohlížeče), takže je lze
spustit i v prostředí bez grafického rozhraní.


Pro vizuální kontrolu průběhu lze testy spustit v headed módu 
s menším zpomalením pro lepší sledování průběhu testů:
```bash
pytest --headed --slowmo 1000
```
