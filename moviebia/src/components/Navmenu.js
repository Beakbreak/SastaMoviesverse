import classes from './Navmenu.module.css';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome'
const Navmenu = props => {
    return (<><div className={classes.navigation}>
        <ul className={classes.ul}>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-house`} /></span>
                    <span className={classes.title}>Home</span>
                </a>
            </li>
            {/* <!-- <li>
                <a href="#">
                    <span className={classes.icon"></span>
                    <span className={classes.icon">Home</span>
                </a>
            </li> --> */}
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-user`} /></span>
                    <span className={classes.title}>Profile</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-wand-magic-sparkles`} /></span>
                    <span className={classes.title}>Suggested</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-heart`} /></span>
                    <span className={classes.title}>Most Rated</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-hashtag`} /></span>
                    <span className={classes.title}>Trending</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-filter`} /></span>
                    <span className={classes.title}>All Genres</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-circle-info`} /></span>
                    <span className={classes.title}>About Us</span>
                </a>
            </li>
            <li className={classes.li}>
                <a href="#" className={classes.a}>
                    <span className={classes.icon}><FontAwesomeIcon icon={`fa-solid fa-right-from-bracket`} /></span>
                    <span className={classes.title}>SignOut</span>
                </a>
            </li>
        </ul>
    </div></>);
}

export default Navmenu;