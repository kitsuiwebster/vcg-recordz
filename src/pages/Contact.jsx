import '../assets/scss/pages/Contact.scss';
import '../assets/scss/index.scss'
import { useTheme } from '../ThemeContext';
import { useTranslation } from 'react-i18next';


function Contact() {
    const { theme } = useTheme();
    const { t } = useTranslation('contact')

    return(
        <div id="contact" className={theme}>
            <div className="contact">
                <h2 className="contact-title">{t('title')}</h2>
                <ul className="contact-list">
                    <li className="contact-list-item">
                        <span className="contact-list-item-label">{t('email')}</span> 
                        <a href="mailto:business@vcgrecordz.eu" className="contact-list-item-link">business@vcgrecordz.eu</a>
                    </li>
                    <li className="contact-list-item">
                        <span className="contact-list-item-label">{t('tel')}</span> 
                        <a href="tel:+33652639088" className="contact-list-item-link">+33 6 52 63 90 88</a>
                    </li>
                    <li className="contact-list-item">
                        <span className="contact-list-item-label">{t('whatsapp')}</span> 
                        <a href="https://wa.me/33652639088" className="contact-list-item-link">{t('send')}</a>
                    </li>
                    <li className="contact-list-item">
                        <span className="contact-list-item-label">{t('telegram')}</span> 
                        <a href="https://t.me/kitsuiwebster" className="contact-list-item-link">{t('send')}</a>
                    </li>
                </ul>
            </div>
        </div>
    )
}

export default Contact