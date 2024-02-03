import React from 'react';
import '../assets/scss/pages/Home.scss';
import '../assets/scss/index.scss'
import { useTranslation } from 'react-i18next';


function Home() {
    const { t } = useTranslation('home');

    return (
        <div id="home">
            <div className='home'>
                <section className='home-vcg'>
                    <h1 className='home-vcg-title'>{t('vcg.title')}</h1>
                </section>
            </div>
        </div>
    );
}

export default Home;
