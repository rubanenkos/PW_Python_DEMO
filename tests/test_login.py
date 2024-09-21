import re
from playwright.sync_api import Page, expect

def test_has_title1(page: Page):
    page.goto("https://playwright.dev/")

    # Expect a title "to contain" a substring.
    expect(page).to_have_title(re.compile("Playwright"))
    page.get_by_role("button", name="Node.js").hover()
    page.get_by_label("Main", exact=True).get_by_role("link", name="Python").click()
    expect(page).to_have_url(re.compile(r".*/python/?"))


