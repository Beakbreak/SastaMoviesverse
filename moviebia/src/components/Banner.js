import classes from './Banner.module.scss';
import Slider from 'react-slick';
import Navbar from './Navbar';
import "slick-carousel/slick/slick.css";
import "slick-carousel/slick/slick-theme.css";
import banimage from "./sampleBanner.jpg";

const Banner = props => {
    var settings = {
        infinite: true,
        fade: true,
        autoplay: true,
        speed: 1000,
        autoplaySpeed: 6000,
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,

    };
    return (<>
        <div>

            <Slider {...settings} className={classes.slider}>
                <div className={classes["img-shadow"]}>
                    <img src={banimage} className={classes.bannerImage} />
                </div>
                <div className={classes["img-shadow"]}>
                    <img src={banimage} className={classes.bannerImage} />
                </div>
                <div className={classes["img-shadow"]}>
                    <img src={banimage} className={classes.bannerImage} />
                </div>
                <div className={classes["img-shadow"]}>
                    <img src={banimage} className={classes.bannerImage} />
                </div>
                <div className={classes["img-shadow"]}>
                    <img src={banimage} className={classes.bannerImage} />
                </div>
                <div className={classes["img-shadow"]}>
                    <img src={banimage} className={classes.bannerImage} />
                </div>
            </Slider></div><Navbar /></>
    );
}
export default Banner;