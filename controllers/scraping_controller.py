from playwright.sync_api import sync_playwright
class Scraping_controller():
    
    def obtener_valores(self,cantidad):
        with sync_playwright() as playwright:
            browser = playwright.chromium.launch()
            page = browser.new_page()
            page.goto("https://listado.mercadolibre.com.ve/computacion/_Container_hcl-computacion-laptops_NoIndex_True")

            page.wait_for_selector("h2.poly-component__title")
            titulos = page.query_selector_all("h2.poly-component__title")[:cantidad]
            print(len(titulos))
            precios = page.query_selector_all("div.poly-price__current")[:cantidad]
            print(len(precios))
            productos = []
            for titulo,precio in zip(titulos,precios):
                
                entero = precio.query_selector("span.andes-money-amount__fraction")
                precio_entero = entero.inner_text() if entero else "0"
                
                decimal = precio.query_selector("span.andes-money-amount__cents")
                precio_decimal = decimal.inner_text() if decimal else "00"
                
                
                productos.append({
                    "descripcion":titulo.inner_text(),
                    "precio": f"{precio_entero}.{precio_decimal}",
                })
                
            browser.close()
            return productos