from playwright.sync_api import sync_playwright
import pytest

def nezbytne_cookies(page, button_text):
    # Button_text je kvůli tomu, abych funkci mohla použít i po přechodu na jinou stránku
    btn_necessary = page.get_by_role("button", name=button_text)
    if btn_necessary.is_visible():
        btn_necessary.click()

@pytest.fixture()
def engeto_page(page):
    # Fixture, která pro každý test otevře stránku engeto.cz a rovnou odmítne cookies
    page.goto("https://engeto.cz/")
    nezbytne_cookies(page, "Souhlasím jen s nezbytnými")
    return page

def test_volne_pozice_sporitelna(engeto_page):
    # Přejdeme na stránku engeto.cz a rovnou odmítneme cookies
    page = engeto_page

    # Najedeme myší na "O nás" a přejdeme do "Zaměstnavatelé"
    page.locator("text=O nás").first.hover()
    page.click("text=Zaměstnavatelé")
    assert page.url == "https://engeto.cz/partnerske-firmy/"

    # U České spořitelny klikneme na "Detail firmy" a přejdeme na detail ČS
    page.click("a[href$='/partnerske-firmy/ceska-sporitelna/']")
    assert page.url == "https://engeto.cz/partnerske-firmy/ceska-sporitelna/"
    assert "Česká spořitelna" in page.locator("h2").first.text_content()

    # Klikneme na "Zobrazit volné pozice", odkaz vede na jobs.cz, kde zase odmítneme cookies
    page.click("text=Zobrazit volné pozice")
    page.wait_for_load_state()
    nezbytne_cookies(page, "Přijmout nezbytné")
    assert "jobs.cz" in page.url

def test_precteni_pribehu_absolventa(engeto_page):
    # Přejdeme na stránku engeto.cz a rovnou odmítneme cookies
    page = engeto_page

    # Najedeme myší na "Kurzy" a klikneme na "Testing Akademie"
    page.get_by_role("link", name="Kurzy", exact=True).hover()
    page.get_by_role("link", name="Testing Akademie | ENGETO").click()
    assert page.url == "https://engeto.cz/testovani-softwaru/"

    # Klikneme na "Příběhy a reference"
    page.click("text=Příběhy a reference")

    # Klikneme na "Přečíst celý příběh"
    page.click("text=Přečíst celý příběh")
    assert page.url == "https://engeto.cz/absolventi/david-langr/"

def test_precteni_webinare_jak_se_stat_testerem(engeto_page):
    # Přejdeme na stránku engeto.cz a rovnou odmítneme cookies
    page = engeto_page

    # Najedeme myší na "Průvodce IT" a klikneme na "Blog"
    page.locator("text=Průvodce IT").first.hover()
    page.click("text=Blog")
    assert page.url == "https://engeto.cz/blog/"

    # Klikneme na filtr "Testing"
    page.click("text=Testing 6")
    assert page.url == "https://engeto.cz/category/testing/"

    # Klikneme na článek "Webinář: Jak se stát software testerem"
    page.click("text=Webinář: Jak se stát software testerem")
    assert page.url == "https://engeto.cz/blog/kariera/webinar-jak-se-stat-software-testerem/"