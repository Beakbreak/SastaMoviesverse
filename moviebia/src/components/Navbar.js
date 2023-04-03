import style from './Navbar.module.css';

const Navbar = props => {
    return (
        <div className={style.Navbar}>
            <img className={style.img} src={require('./home-logo.png')} alt='logo' />
            <h2 className={style.hello}>Hello, <b className={style.username}>Dhruv</b></h2>
        </div>
    )
}

export default Navbar;