import '../assets/scss/layouts/Layout.scss';
import React, { useState, useEffect } from 'react';
import menuIcon from '../assets/images/menu.png'
import { useTheme } from '../ThemeContext';

import { useTranslation } from 'react-i18next';
import ukFlag from '../assets/images/flags/uk.png'
import frenchFlag from '../assets/images/flags/fr.png'
import logo from '../assets/images/white-logo.png'; 


function Layout({ children }) {
    const { t, i18n } = useTranslation('layout');
    const [isNavOpen, setIsNavOpen] = useState(false);
    const { theme, toggleTheme } = useTheme();
    const [isLangMenuOpen, setIsLangMenuOpen] = useState(false);

    const getStoredLanguage = () => {
        const storedLang = localStorage.getItem('i18nextLng');
        return storedLang || 'en';
    };

    const [currentLanguage, setCurrentLanguage] = useState(getStoredLanguage());
    const [currentFlag, setCurrentFlag] = useState(currentLanguage === 'en' ? ukFlag : frenchFlag);

    useEffect(() => {
        i18n.changeLanguage(currentLanguage);
        localStorage.setItem('i18nextLng', currentLanguage);
    }, [currentLanguage, i18n]);

    const toggleLangMenu = () => setIsLangMenuOpen(!isLangMenuOpen);

    const changeLanguage = (lang) => {
        setCurrentLanguage(lang);
        setCurrentFlag(lang === 'en' ? ukFlag : frenchFlag);
        setIsLangMenuOpen(false);
    };
    

    const toggleNav = () => setIsNavOpen(!isNavOpen);

    return (
        <>
            <div className={`layout ${theme}`}>
                <header className="layout-header">
                    <div className='layout-header-logo-container'>
                        <img src={logo} alt="Logo" className='layout-header-logo' />
                    </div>
                    <div className="layout-header-mobile" onClick={toggleNav}>
                        <img loading="lazy" alt="Menu Icon" src={menuIcon} className='layout-header-icon'></img>
                    </div>
                    <nav className={`layout-header-nav ${isNavOpen ? 'open' : ''}`}>
                        <ul className='layout-header-nav-ul'>
                            <li className="layout-header-nav-ul-li"> <a className="layout-header-nav-ul-li-a" href="/" >{t('header.home')}</a></li>
                            <li className="layout-header-nav-ul-li"> <a className="layout-header-nav-ul-li-a" href="/contact">{t('header.contact')}</a></li>
                        </ul>
                    </nav>
                    <div className="layout-header-toggle">
                        <div className="layout-header-toggle-language">
                            <img loading="lazy" src={currentFlag} alt="Language" onClick={toggleLangMenu} className="layout-header-toggle-language-icon" />
                            {isLangMenuOpen && (
                                <div className="layout-header-toggle-language-menu">
                                    {currentLanguage !== 'en' && (
                                        <img loading="lazy" className='layout-header-toggle-language-menu-icon'
                                        src={ukFlag} alt="United Kingdom flag" onClick={() => changeLanguage('en')}/>
                                    )}
                                    {currentLanguage !== 'fr' && (
                                        <img loading="lazy" className='layout-header-toggle-language-menu-icon'
                                        src={frenchFlag} alt="France flag" onClick={() => changeLanguage('fr')}/>
                                    )}
                                </div>
                            )}
                        </div>
                        <button onClick={toggleTheme} className={`layout-header-toggle-theme ${theme}`}>
                        </button>
                    </div>
                </header>

                <main className='layout-main'>
                    {children}
                </main>

                <footer className="layout-footer">
                    <p className='layout-footer-text'>{t('footer.copyright')}</p>
                </footer>
            </div>
        </>
    );
}

export default Layout;
