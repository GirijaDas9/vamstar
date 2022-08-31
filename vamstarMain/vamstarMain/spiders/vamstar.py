
import scrapy


class QuotestoSpider(scrapy.Spider):
    name = 'vamstar'
    allowed_domains = ['diariomunicipal.sc.gov.br']
    start_urls = ['https://www.diariomunicipal.sc.gov.br/?r=site/index&q=abertura+categoria%3ALicita%C3%A7%C3%B5es&AtoASolrDocument_page=1']
    base_url = "https://www.diariomunicipal.sc.gov.br"

    def parse(self, response):
        all_span = response.css('span.quiet')
        for i in all_span:
            date = i.css('::text').extract()
            for i in date:
                if "/" in i:
                    date = i
        visual = response.css('a[target="_blank"]::attr(href)').extract()
        for j in visual:
            if '/?r=site/' in j:
                visual_data = self.base_url+j
        result = response.css('p>a::attr(href)').extract()
        for k in result:
            result_data = self.base_url+k
        all_h4 = response.css('h4')
        for data in all_h4:
            title = data.css('a::text')[0].extract()
            pdf = data.css('a::attr(href)')[0].extract()

            yield {
                'Title_text':title,
                'PDF_Link':pdf,
                'Publication Date':date,
                'Visualizar Ato Link':visual_data,
                'Abrir/Salvar Original':pdf,
                'Resultados Semelhantes...':result_data
            }
        next_page = self.base_url+response.css('li.next>a::attr(href)').extract_first()
        if next_page is not None:
            yield response.follow(next_page, callback= self.parse)