import style from './Navbar.module.css';

const Navbar = props => {
    return (
        <div className={style.Navbar}>
            <img src={require('./main-logo1.png')} />

            <div className={style.cards}>
                <p>Genres</p>
                <div className={style.options}>
                    <p>Action</p>
                    <p>Romance</p>
                    <p>Comedy</p>
                    <p>Adventure</p>
                    <p>Fantasy</p>
                    <p>Horror</p>
                    <p>Thriller</p>
                </div>
            </div>

            <div className={style.cards}>
                <p>Language</p>
                <div className={style.options}>
                    <p>English</p>
                    <p>Hindi</p>
                    <p>Marathi</p>
                    <p>Spanish</p>
                    <p>Italian</p>
                    <p>Persian</p>
                    <p>German</p>
                </div>
            </div>

            <div className={style.cards}>
                <p>OTT</p>
                <div className={style.options}>
                    <p>Netflix</p>
                    <p>HULU</p>
                    <p>Hotstar</p>
                    <p>Amazon Prime Video</p>
                    <p>MX Player</p>
                    <p>Disney Plus</p>
                    <p>HBO</p>
                </div>
            </div>

            <input type="text" />
            <p className={style.p}>Logout</p>
        </div>
    )
}

export default Navbar;