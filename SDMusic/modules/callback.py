from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton, Chat, CallbackQuery
from SDMusic.helpers.decorators import authorized_users_only
from SDMusic.config import BOT_NAME, BOT_USERNAME, OWNER_NAME, SUPPORT_GROUP, UPDATES_CHANNEL, ASSISTANT_NAME
from SDMusic.modules.play import cb_admin_check


@Client.on_callback_query(filters.regex("cbstart"))
async def cbstart(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 **Merhaba, Ben {query.message.from_user.mention}** \n 
 
 **[{BOT_NAME}](https://t.me/{BOT_USERNAME}) Yeni Telegram Sesli Sohbet Yoluyla Gruplarda Müzik Çalmanıza İzin Vermeye Yarayan Bir Botum !**
 
 » Komutlar Düğmesine Tıklayarak Botun Tüm Komutlarını ve Nasıl Çalıştıklarını Öğrenin !**
 
 **Bu Botun Tüm Özellikleri Hakkında Bilgi İçin, Sadece**
</b>""",
        reply_markup=InlineKeyboardMarkup(
            [ 
                [
                    InlineKeyboardButton(
                        "➕ Beni Bir Gruba Ekle ➕", url=f"https://t.me/{BOT_USERNAME}?startgroup=true")
                ],[
                    InlineKeyboardButton(
                        "Nasıl Kullanılır ? ", callback_data="cbhowtouse")
                ],[
                    InlineKeyboardButton(
                         "Komutlar Yardım ?", callback_data="cbcmds"
                    ),
                    InlineKeyboardButton(
                        "👤 Geliştirici ", url=f"https://t.me/theezelboss")
                ],[
                    InlineKeyboardButton(
                        "👥 Support", url=f"https://t.me/ezelhome"
                    ),
                    InlineKeyboardButton(
                        "📢 Kanal ", url=f"https://t.me/ezelizm")
                ],[
                    InlineKeyboardButton(
                        "❌ Çıkış", callback_data="close"
                    )
                ]
            ]
        ),
     disable_web_page_preview=True
    )


@Client.on_callback_query(filters.regex("cbhelp"))
async def cbhelp(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 Merhaba Yardım Menüsüne Hoşgeldiniz !</b>

**Bu Menüde Birkaç Kullanılabilir Komut Menüsü Açabilirsiniz, Her Komut Menüsünde Ayrıca Her Komutun Kısa Bir Açıklaması Vardır.**

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Basic Commands", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Advanced Commands", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Admin Commands", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "Sudo Commands", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Owner Commands", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Fun Commands", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbguide"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbbasic"))
async def cbbasic(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Temel Komutlar</b>

🎧 [ Grup Müzik Komutları ]
- `/play` `(Şarkı Adı)` - `Youtube'dan Şarkı Çal`
- `/ytpplay` `(Şarkı Adı)` - `Doğrudan Youtube'dan Şarkı Çal` 
- `/playlist` - `Sıradaki Liste Şarkısını Göster`
- `/song` `(Şarkı Adı)` - `Youtube'dan Şarkı İndir`
- `/search` `(Video Adı)` - `Youtube Detaylı Arama Videosu`
- `/video` `(Video Adı)` - `Youtube Detaylı Video İndir`
- `/lyrics` - `(Şarkı Adı)` `Şarkı Sözleri Kazıyıcı`

🎧 [ Kanal Müzik Komutları ]
- `/cplay` - `Kanal Sesli Sohbetinde Müzik Akışı Yapın`
- `/cplayer` - `Şarkıyı Akışta Göster`
- `/cpause` - `Müzik Akışını Duraklat`
- `/cresume` - `Akışa Devam Etme Duraklatıldı`
- `/cskip` - `Akışı Bir Sonraki Şarkıya Atla`
- `/cend` - `Müzik Akışını Sonlandır`
- `/admincache` - `Yönetici Önbelleğini Yenile`
- `/userbotjoin`: Asistanı @{ASSISTANT_NAME} Sohbetinize Davet Eder

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadvanced"))
async def cbadvanced(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Gelişmiş Komutlar</b>

`/start` `(Grup İçerisinde)` - `Botun Canlı Durumunu Görün`
`/reload` - `Botu Yeniden Yükleyin Ve Yönetici Listesini Yenileyin`
`/admincache` - `Yönetici Önbelleğini Yenile`
`/ping` - `Bot Ping Durumunu Kontrol Et`
`/uptime` - `Bot Çalışma Süresi Durumunu Kontrol Edin`
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbadmin"))
async def cbadmin(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<bYönetici Komutları</b>

`/player` - `Müzik Çalma Durumunu Göster`
`/pause` - `Öüzik Akışını Duraklat`
`/resume` - `Devam Ettir`
`/skip` - `Sonraki Şarkıya Geç`
`/end` - `Müzik Akışını Durdur`
`/userbotjoin` - `Asistanı Grubunuza Katılmaya Davet Edin`
`/auth` - `Müzik Botunu Kullanmak İçin Yetkili Kullanıcı`
`/deauth` - `Müzik Botu Kullanmak İçin Yetkisiz`
`/control` - `Oynatıcı Ayarları Panelini Açın`
`/delcmd` `(on | off)` - `Del Cmd Özelliğini Etkinleştir / Devre Dışı Bırak`
`/musicplayer` `(on / off)` - `Grubunuzdaki Müzik Çaları Etkinleştir / Devre Dışı Bırak`
`/b` `and` `/tb` `(ban / temporary ban)` - `Grupta Kalıcı Veya Geçici Olarak Yasaklanan Kullanıcı`
`/ub` - `Bansız Kullanıcıya Gruptan Banlandın`
`/m` `and` `/tm` `(mute / temporary mute)` - `Grupta Kalıcı Olarak Veya Geçici Olarak Sessize Alınan Kullanıcıyı Sessize Al`
`/um` - `Grupta Sessize Aldığınız Kullanıcının Sesini Açmak İçin`

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbsudo"))
async def cbsudo(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Sudo Komutları</b>

`/userbotleaveall` - `Asistana Tüm Gruptan Ayrılmasını Emredin`
`/gcast` - `Asistandan Bir Yayın Mesajı Gönder`
`/stats` - `Bot İstatistiğini Göster`
`/rmd` - `İndirilen Tüm Dosyaları Kaldır`
`/clean` - `Tüm Ham Dosyaları Kaldır`

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbowner"))
async def cbowner(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Sahip Komutları</b>

`/stats` - `Bot İstatistiğini Göster`
`/broadcast` - `Bottan Yayın Mesajı Gönder`
`/block` `(user id - duration - reason)` - `Botunuzu Kullanması İçin Kullanıcıyı Engelle`
`/unblock` `(user id - reason)` - `Botunuzu Kullandığı İçin Engellediğiniz Kullanıcının Engellemesini Kaldırın`
`/blocklist` - `Botunuzu Kullanmak İçin Engellenen Kullanıcı Listesini Göster`
📝 Not : Bu Botun Sahip Olduğu Tüm Komutlar, İstisnasız Olarak Botun Sahibi Tarafından Yürütülebilir.

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbfun"))
async def cbfun(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Eğlenceli Komutlar</b>

`/chika` - `Kendin Kontrol Et`
`/wibu` - `Kendin Kontrol Et`
`/asupan` - `Kendin Kontrol Et`
`/truth` - `Kendin Kontrol Et`
`/dare` - `Kendin Kontrol Et`

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbhelp"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbguide"))
async def cbguide(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Nasıl Kullanılır 🤔:

1.) İlk Önce Beni Grubunuza Ekleyin.
2.) Sonra Beni Yönetici Olarak Terfi Ettir Ve Anonim Yönetici Hariç Tüm İzinleri Ver.
3.) Ekle @{ASSISTANT_NAME} Grubunuza Davet Etmek İçin /userbotjoin Yazın.
4.) Müzik Çalmaya Başlamadan Önce Sesli Sohbeti Açın.

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "All Commads", callback_data="cbhelp"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Çıkış ", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("close"))
async def close(_, query: CallbackQuery):
    await query.message.delete()


@Client.on_callback_query(filters.regex("cbback"))
@cb_admin_check
async def cbback(_, query: CallbackQuery):
    await query.edit_message_text(
        "**Bot'un Kontrol Menüsü :**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⏸ Duraklat", callback_data="cbpause"
                    ),
                    InlineKeyboardButton(
                        "▶️ Devam Et", callback_data="cbresume"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "⏩ Atla", callback_data="cbskip"
                    ),
                    InlineKeyboardButton(
                        "⏹ Son", callback_data="cbend"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Anti Komutlar", callback_data="cbdelcmds"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Grup Araçları", callback_data="cbgtools"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "❌ Çıkış", callback_data="close"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbgtools"))
@cb_admin_check
@authorized_users_only
async def cbgtools(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>Özellik Bilgileri :</b>

🔥 **Özellikler:** Bu Özellik Grubunuzdaki Kullanıcıların Sesini Kapatabilen, Sesi Kapatan, Yasağını Kaldıran, Sesini Açabilen İşlevleri İçerir.

Ayrıca Yur Goup Üyeleri İçin Yasaklama ve Sesi Kapatma Cezaları İçin Bir Süre Belirleyebilirsiniz, Böylece Cezayı Seçilmiş Süreyle Serbest Bırakabilirler.

📝 **Kullanım:**

1️⃣ Kullanıcıyı Grubunuzdan Yasaklayın Veya Geçici Olarak Yasaklayın:
   » type `/b username/reply to message` Kalıcı Ban
   » type `/tb username/reply to message/duration` Kullanıcıyı Geçici Olarak Yasakla
   » type `/ub username/reply to message` Kullanıcı Yasağını Kaldır
2️⃣ Grubunuzdaki Kullanıcıyı Sessize Alın Veya Geçici Olarak Sessize Alın:
   » type `/m username/reply to message` Kalıcı Olarak Sessize Al
   » type `/tm username/reply to message/duration` Kullanıcıyı Geçici Olarak Sessize Al
   » type `/um username/reply to message` Kullanıcının Sesini Aç
📝 Not : cmd /b, /tb and /ub & /m, /tm ve /um, Grubunuzdaki Kullanıcıyı Sessize Alma/Sessizden Açma Komutlarıdır..
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbdelcmds"))
@cb_admin_check
@authorized_users_only
async def cbdelcmds(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>This is The Feature Information :</b>
        
**🔥 Özellikler:** Gruplarda İstenmeyen Postalardan Kaçınmak İçin Kullanıcılar Tarafından Gönderilen Tüm Komutları Silin!
❔ usage:**
 1️⃣ Özelliği Açmak İçin:
     » type `/delcmd on`
    
 2️⃣  Özelliği Kapatmak İçin:
     » type `/delcmd off`
      
POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbback"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbcmds"))
async def cbhelps(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""<b>👋 Merhaba, Yardım Menüsüne Hoş Geldiniz !</b>

**Bu Menüde Birkaç Mevcut Komut Menüsünü Açabilirsiniz, Her Komut Menüsünde Ayrıca Her Komutun Kısa Bir Açıklaması Bulunmaktadır.**

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Temel Komutlar", callback_data="cbbasic"
                    ),
                    InlineKeyboardButton(
                        "Gelişmiş Komutlar", callback_data="cbadvanced"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Yönetici Komutları", callback_data="cbadmin"
                    ),
                    InlineKeyboardButton(
                        "Sudo Komutları", callback_data="cbsudo"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Sahip Komutları", callback_data="cbowner"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Eğlenceli Komutlar", callback_data="cbfun"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "Geri", callback_data="cbstart"
                    )
                ]
            ]
        )
    )


@Client.on_callback_query(filters.regex("cbhowtouse"))
async def cbguides(_, query: CallbackQuery):
    await query.edit_message_text(
        f"""Nasıl Kullanılır 🤔:

1.) İlk Önce Beni Grubunuza Ekleyin.
2.) Sonra Beni Yönetici Olarak Terfi Ettir Ve Anonim Yönetici Hariç Tüm İzinleri Ver.
3.) Ekle @{ASSISTANT_NAME} Grubunuza Davet Etmek İçin /userbotjoin Yazın.
4.) Müzik Çalmaya Başlamadan Önce Sesli Sohbeti Açın.

POWERD BY {BOT_NAME} A.I__""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Back", callback_data="cbstart"
                    )
                ]
            ]
        )
    )
