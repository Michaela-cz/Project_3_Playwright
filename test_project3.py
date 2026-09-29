from playwright.sync_api import expect
import pytest

def nezbytne_cookies(page, button_text):
    """ Povolení pouze nezbytných cookies, pokud se okno s cookies zobrazí.
    Button_text je kvůli tomu, abych funkci mohla použít i po přechodu na jinou stránku.
    Krátce se čeká na zobrazení cookies okna, aby test nespadl, pokud by načtení stránky trvalo. """
    btn_necessary = page.get_by_role("button", name=button_text)
    try:
        btn_necessary.wait_for(state="visible", timeout=3000)
        btn_necessary.click()
    except:
        pass # Pokud se lišta z nějakého důvodu nezobrazí, test i přesto projde

@pytest.fixture()
def engeto_page(page):
    """ Fixture, která pro každý test otevře stránku engeto.cz a rovnou odmítne cookies """
    page.goto("https://engeto.cz/")
    nezbytne_cookies(page, "Souhlasím jen s nezbytnými")
    return page

def test_volne_pozice_sporitelna(engeto_page):
    # Přejdeme na stránku engeto.cz a rovnou odmítneme cookies
    page = engeto_page

    # Najedeme myší na "O nás" a přejdeme do "Zaměstnavatelé"
    page.get_by_text("O nás", exact=True).first.hover()
    page.get_by_role("link", name="Zaměstnavatelé").click()
    expect(page).to_have_url("https://engeto.cz/partnerske-firmy/")

    # U České spořitelny klikneme na "Detail firmy" a přejdeme na detail ČS
    page.locator("a[href$='/partnerske-firmy/ceska-sporitelna/']").click()
    expect(page).to_have_url("https://engeto.cz/partnerske-firmy/ceska-sporitelna/")
    expect(page.locator("h2").first).to_contain_text("Česká spořitelna")

    # Klikneme na "Zobrazit volné pozice", odkaz vede na jobs.cz, kde zase odmítneme cookies
    page.get_by_text("Zobrazit volné pozice").click()
    page.wait_for_load_state()
    nezbytne_cookies(page, "Přijmout nezbytné")
    assert "jobs.cz" in page.url

def test_precteni_pribehu_absolventa(engeto_page):
    # Přejdeme na stránku engeto.cz a rovnou odmítneme cookies
    page = engeto_page

    # Najedeme myší na "Kurzy" a klikneme na "Testing Akademie"
    page.get_by_role("link", name="Kurzy", exact=True).hover()
    page.get_by_role("link", name="Testing Akademie | ENGETO").click()
    expect(page).to_have_url("https://engeto.cz/testovani-softwaru/")

    # Klikneme na "Příběhy a reference"
    page.get_by_role("link", name="Příběhy a reference").click()

    # Klikneme na "Přečíst celý příběh"
    page.get_by_role("link", name="Přečíst celý příběh").first.click()
    assert "absolventi" in page.url

def test_precteni_webinare_jak_se_stat_testerem(engeto_page):
    # Přejdeme na stránku engeto.cz a rovnou odmítneme cookies
    page = engeto_page

    # Najedeme myší na "Průvodce IT" a klikneme na "Blog"
    page.get_by_role("link", name="Průvodce IT", exact=True).first.hover()
    page.locator("a[href='https://engeto.cz/blog/']").first.click()
    expect(page).to_have_url("https://engeto.cz/blog/")

    # Klikneme na filtr "Testing"
    page.locator("a[href='https://engeto.cz/category/testing/']").click()
    expect(page).to_have_url("https://engeto.cz/category/testing/")

    # Klikneme na článek "Webinář: Jak se stát software testerem"
    page.get_by_role("link", name="Webinář: Jak se stát software testerem").first.click()
    expect(page).to_have_url("https://engeto.cz/blog/kariera/webinar-jak-se-stat-software-testerem/")